from PyQt5 import QtCore, QtGui, QtWidgets


class MsgView(QtWidgets.QWidget):

    def __init__(self):
        super(MsgView, self).__init__()
        self.msg_widget = QtWidgets.QWidget()
        self.msg_widget.setObjectName("msg_widget")
        self.setGeometry(QtCore.QRect(0, 0, 431, 161))
        self.msg_background = QtWidgets.QLabel(self.msg_widget)
        self.msg_background.setGeometry(QtCore.QRect(0, 0, 291, 161))
        self.msg_background.setStyleSheet("background: url(custom_qt_classes/img_source/m3.png)")
        self.msg_background.setText("")
        self.msg_background.setObjectName("msg_background")
        self.username_label = QtWidgets.QLabel(self.msg_widget)
        self.username_label.setGeometry(QtCore.QRect(20, 10, 131, 16))
        self.username_label.setObjectName("username_label")
        self.username_label.setStyleSheet("font: 75 8pt 'MS Shell Dlg 2';")
        self.msg_label = QtWidgets.QTextBrowser(self.msg_widget)
        self.msg_label.setStyleSheet("background-color: rgb(14, 165, 189);")
        self.msg_label.setGeometry(QtCore.QRect(20, 30, 251, 81))
        self.msg_label.setObjectName("msg_label")
        # self.msg_label.setWordWrap(True)
        grid_box = QtWidgets.QGridLayout()
        grid_box.addWidget(self.msg_widget, 1, 0)

        self.setLayout(grid_box)
        self.show()

    def sizeHint(self):
        return QtCore.QSize(300, 185)

    def set_username(self, username):
        self.username_label.setText(username)

    def set_msg(self, msg):
        self.msg_label.setText(msg)
