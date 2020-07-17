import socket
import errno
import sys
from PyQt5.QtCore import pyqtSignal, QThread


class Connection(QThread):
    HEADER_LENGTH = 10
    IP = "127.0.0.1"
    PORT = 8000

    # signals
    get_msg = pyqtSignal(str, str, str, str)

    def __init__(self):
        super().__init__()
        self.username = ""
        self.client_socket = None

    def set_username_start_connect(self, username):
        self.username = username
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.IP, self.PORT))
        self.client_socket.setblocking(False)

        username_encode = username.encode('utf_8')
        username_header = f'{len(username_encode):<{self.HEADER_LENGTH}}'.encode("utf_8")
        self.client_socket.send(username_header + username_encode)

    def send_message(self, message):
        if message:
            message = message.encode("utf_8")
            message_header = f'{len(message):<{self.HEADER_LENGTH}}'.encode("utf_8")
            self.client_socket.send(message_header + message)

    @property
    def get_message(self):
        username_header = self.client_socket.recv(self.HEADER_LENGTH)
        if not len(username_header):
            print("connection close by the server")
            return None, None, None

        username_length = int(username_header.decode("utf_8").strip())
        username_encode = self.client_socket.recv(username_length).decode("utf_8")

        message_header = self.client_socket.recv(self.HEADER_LENGTH)
        message_length = int(message_header.decode("utf_8").strip())
        message = self.client_socket.recv(message_length).decode("utf_8")

        online_header = self.client_socket.recv(self.HEADER_LENGTH)
        online_length = int(online_header.decode("utf_8").strip())
        online = self.client_socket.recv(online_length).decode("utf_8")

        kind_header = self.client_socket.recv(self.HEADER_LENGTH)
        kind_length = int(kind_header.decode("utf_8").strip())
        kind = self.client_socket.recv(kind_length).decode("utf_8")

        return username_encode, message, online, kind

    def run(self):
        while True:
            try:
                while True:
                    username, message, count_online, kind = self.get_message
                    if username is None:
                        sys.exit()

                    self.get_msg.emit(username, message, count_online, kind)

            except IOError as e:
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print('Reading Error ' + str(e))
                    break
                    # sys.exit()
                continue

            except Exception as e:
                print('General Error ' + str(e))
                break
                # sys.exit()
