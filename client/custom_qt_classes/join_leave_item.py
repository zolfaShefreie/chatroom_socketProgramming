from PyQt5 import QtCore, QtGui, QtWidgets


class JLItem(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.widget = QtWidgets.QWidget()
        self.widget.setGeometry(QtCore.QRect(0, 0, 431, 51))
        self.widget.setObjectName("widget")
        self.l_j_message = QtWidgets.QLabel(self.widget)
        self.l_j_message.setGeometry(QtCore.QRect(80, 10, 261, 31))
        self.l_j_message.setStyleSheet("background-color: rgb(1, 17, 38);\n"
                                       "font: italic 12pt \"Monotype Corsiva\";\n"
                                       "color: rgb(171, 171, 171);")
        self.l_j_message.setObjectName("label")
        self.l_j_message.setAlignment(QtCore.Qt.AlignCenter)
        grid_box = QtWidgets.QGridLayout()
        grid_box.addWidget(self.widget, 1, 0)

        self.setLayout(grid_box)
        self.show()

    def sizeHint(self):
        return QtCore.QSize(300, 80)

    def set_msg(self, is_joined, username):
        if is_joined:
            msg = username + " joined the chat group"
        else:
            msg = username + " left the chat group"
        self.l_j_message.setText(msg)
