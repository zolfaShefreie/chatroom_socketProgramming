
from PyQt5 import QtCore, QtGui, QtWidgets
from custom_qt_classes.main_fram import Ui_Form
from custom_qt_classes.widget import CustomForm
from client import Connection


class MainWindow(CustomForm, Ui_Form):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.pressing = False
        self.setMouseTracking(True)

        self.username_str = ""
        self.connect = Connection()

        # connect signals to listeners
        self.close_btn.clicked.connect(self.close_window)
        self.username_btn.clicked.connect(self.start)
        self.send_btn.clicked.connect(self.send_msg)
        self.left_btn.clicked.connect(self.left)
        self.cancel_btn.clicked.connect(self.close_window)

        self.connect.finished.connect(self.disconnect_to_server)
        self.connect.get_msg.connect(self.show_server_msg)

    def show_error_box(self, msg):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setText(msg)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        msg_box.setStyleSheet("""
        QMessageBox {
            background-color: rgb(1, 14, 30);
        }

        QMessageBox QLabel {
            color: rgb(200, 200, 200);
        }
        QMessageBox QPushButton {
            background-color: rgb(3, 14, 30);
            color: rgb(200, 200, 200);
        }""")
        msg_box.exec_()
        msg_box.show()

    @QtCore.pyqtSlot()
    def left(self):
        self.show_error_box(msg="you left the chat group")
        self.close()
        self.connect.quit()

    @QtCore.pyqtSlot()
    def send_msg(self):
        txt = self.msg_txt_edit.toPlainText().__str__()
        if txt.split():
            self.msg_txt_edit.clear()
            try:
                self.connect.send_message(txt)
                self.listWidget.add_custom_item(1, self.username_str, txt)
            except Exception as e:
                print(str(e))
                self.show_error_box("can't connect to server please try later")
                self.close()
                self.connect.quit()

    @QtCore.pyqtSlot(str, str, str, str)
    def show_server_msg(self, username, msg, online, kind):
        self.listWidget.add_custom_item(int(kind), username, msg)
        self.online.setText(online+" online")

    @QtCore.pyqtSlot()
    def disconnect_to_server(self):
        self.show_error_box("disconnection error")
        self.close()

    @QtCore.pyqtSlot()
    def start(self):
        self.username_str = self.username_line.text()
        if self.username_str.split():
            try:
                self.connect.set_username_start_connect(self.username_str)
                self.connect.start()
                self.stackedWidget.setCurrentIndex(1)
                self.listWidget.add_custom_item(2, "You", "")
            except ConnectionRefusedError:
                self.show_error_box("can't connect to server please try later")
            except Exception as e:
                print(str(e))
        else:
            self.show_error_box("the username is empty")

    @QtCore.pyqtSlot()
    def close_window(self):
        self.connect.quit()
        self.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())



