import socket
import select


class Server(object):
    HEADER_LENGTH = 10
    IP = "127.0.0.1"
    PORT = 8000
    socket_list = []
    clients = {}

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.server_socket.bind((self.IP, self.PORT))
        self.server_socket.listen(5)

        self.socket_list.append(self.server_socket)

    def receive_msg(self, client_socket):
        try:
            header_msg = client_socket.recv(self.HEADER_LENGTH)
            if not len(header_msg):
                return False

            message_length = int(header_msg.decode("utf_8").strip())
            return {"header": header_msg, "data": client_socket.recv(message_length)}

        except:
            return False

    def generate_count_msg(self):
        online = str(len(self.clients))
        online_header = f'{len(online):<{self.HEADER_LENGTH}}'.encode("utf_8")
        online = online.encode("utf_8")
        return {"header": online_header, "data": online}

    def generate_type_msg(self, kind):
        type_msg = str(kind)
        type_header = f'{len(type_msg):<{self.HEADER_LENGTH}}'.encode("utf_8")
        type_msg = type_msg.encode("utf_8")
        return {"header": type_header, "data": type_msg}

    def send_to_all(self, notified_socket, user, message, online, kind):
        for client_socket in self.clients:
            if client_socket != notified_socket:
                client_socket.send(user['header'] + user['data'] + message['header'] + message['data'] +
                                   online['header'] + online['data'] + kind['header'] + kind['data'])

    def generate_join_leave_msg(self, is_joined):
        if is_joined:
            message = "joined the chat group"
        else:
            message = "left the chat group"
        message_header = f'{len(message):<{self.HEADER_LENGTH}}'.encode("utf_8")
        message = message.encode("utf_8")
        return {"header": message_header, "data": message}

    def leave(self, notified_socket):
        self.socket_list.remove(notified_socket)
        user = self.clients[notified_socket]
        msg = self.generate_join_leave_msg(is_joined=False)
        del self.clients[notified_socket]
        online = self.generate_count_msg()
        kind = self.generate_type_msg(kind=3)
        self.send_to_all(notified_socket, user, msg, online, kind)

    def join(self, client_socket):
        user = self.receive_msg(client_socket)
        if not user:
            return None

        self.socket_list.append(client_socket)
        self.clients[client_socket] = user
        msg = self.generate_join_leave_msg(is_joined=True)
        online = self.generate_count_msg()
        kind = self.generate_type_msg(kind=2)
        self.send_to_all(client_socket, user, msg, online, kind)

        return user

    def send_msg(self, notified_socket, message):
        online = self.generate_count_msg()
        kind = self.generate_type_msg(kind=0)
        user = self.clients[notified_socket]
        self.send_to_all(notified_socket, user, message, online, kind)

    def run_server(self):
        while True:
            read_socket, _, exception_socket = select.select(self.socket_list, [], self.socket_list)
            for notified_socket in read_socket:
                if notified_socket == self.server_socket:
                    client_socket, client_addr = self.server_socket.accept()
                    user = self.join(client_socket)
                    if not user:
                        continue

                    print(f"Accepted new connection from {client_addr[0]}: {client_addr[1]} "
                          f" username: {user['data'].decode('utf_8')}")

                else:
                    message = self.receive_msg(notified_socket)
                    if not message:
                        print(f"close connection from {self.clients[notified_socket]['data'].decode('utf_8')}")
                        self.leave(notified_socket)
                        continue

                    user = self.clients[notified_socket]
                    print(f"receive message from {user['data'].decode('utf_8')}: {message['data'].decode('utf_8')}")
                    self.send_msg(notified_socket, message)

            for notified_socket in exception_socket:
                self.leave(notified_socket)

