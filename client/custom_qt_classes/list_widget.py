from PyQt5 import QtCore, QtGui, QtWidgets
from .msg_oth_item_list import MsgView
from .msg_item_list import MsgView2
from .join_leave_item import JLItem


class CustomList(QtWidgets.QListWidget):

    def __init__(self, parent):
        super(CustomList, self).__init__(parent)
        self.style_str = """
        QScrollBar:vertical {              
            border: none;
            background:white;
            width:3px;
            margin: 0px 0px 0px 0px;
        }
        QScrollBar::handle:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));
            min-height: 0px;
        }
        QScrollBar::add-line:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));
            height: 0px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }
        QScrollBar::sub-line:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));
            height: 0 px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }
        """

    def set_background_img(self, path):
        style = """QListWidget{
            background: url(""" + path + """);    
        }\n""" + self.style_str
        self.setStyleSheet(style)

    def add_custom_item(self, kind, username, msg):
        if kind == 0:
            custom_item = MsgView()
            custom_item.set_username(username)
            custom_item.set_msg(msg)
            item = QtWidgets.QListWidgetItem(self)
            item.setSizeHint(custom_item.sizeHint())
            self.addItem(item)
            self.setItemWidget(item, custom_item)

        elif kind == 1:
            custom_item = MsgView2()
            custom_item.set_msg(msg)
            item = QtWidgets.QListWidgetItem(self)
            item.setSizeHint(custom_item.sizeHint())
            self.addItem(item)
            self.setItemWidget(item, custom_item)

        elif kind == 2:
            custom_item = JLItem()
            custom_item.set_msg(is_joined=True, username=username)
            item = QtWidgets.QListWidgetItem(self)
            item.setSizeHint(custom_item.sizeHint())
            self.addItem(item)
            self.setItemWidget(item, custom_item)

        elif kind == 3:
            custom_item = JLItem()
            custom_item.set_msg(is_joined=False, username=username)
            item = QtWidgets.QListWidgetItem(self)
            item.setSizeHint(custom_item.sizeHint())
            self.addItem(item)
            self.setItemWidget(item, custom_item)

        self.scrollToBottom()

