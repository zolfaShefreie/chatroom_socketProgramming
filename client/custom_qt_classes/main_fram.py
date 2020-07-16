
from PyQt5 import QtCore, QtGui, QtWidgets
import os

from .list_widget import CustomList


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(448, 938)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 40, 451, 901))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.username_btn = QtWidgets.QPushButton(self.page)
        self.username_btn.setGeometry(QtCore.QRect(240, 480, 161, 41))
        self.username_btn.setStyleSheet("background-color: rgb(68, 135, 138);\n"
                                        "font: italic 12pt \"Monotype Corsiva\";\n"
                                        "")
        self.username_btn.setObjectName("pushButton")
        self.username_line = QtWidgets.QLineEdit(self.page)
        self.username_line.setGeometry(QtCore.QRect(50, 380, 361, 41))
        self.username_line.setStyleSheet("background-color: rgb(127, 176, 155);")
        self.username_line.setText("")
        self.username_line.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(100, 290, 231, 61))
        self.label.setStyleSheet("font: italic 12pt \"Monotype Corsiva\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 471, 941))
        self.label_2.setStyleSheet("background: url(custom_qt_classes/img_source/img2.png)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.cancel_btn = QtWidgets.QPushButton(self.page)
        self.cancel_btn.setGeometry(QtCore.QRect(70, 480, 161, 41))
        self.cancel_btn.setStyleSheet("background-color: rgb(68, 135, 138);\n"
                                      "font: italic 12pt \"Monotype Corsiva\";")
        self.cancel_btn.setObjectName("pushButton_2")
        self.label_2.raise_()
        self.username_btn.raise_()
        self.username_line.raise_()
        self.label.raise_()
        self.cancel_btn.raise_()
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")

        self.listWidget = CustomList(self.page_2)
        self.listWidget.setGeometry(QtCore.QRect(0, 70, 451, 781))
        self.listWidget.set_background_img("custom_qt_classes/img_source/img2_2.png")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(-10, 0, 471, 941))
        self.label_3.setStyleSheet("background: url(custom_qt_classes/img_source/img2_2.png)")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.send_btn = QtWidgets.QToolButton(self.page_2)
        self.send_btn.setGeometry(QtCore.QRect(400, 850, 51, 51))
        self.send_btn.setStyleSheet("background-color: rgb(88, 172, 174);")
        self.send_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("custom_qt_classes/img_source/send.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_btn.setIcon(icon)
        self.send_btn.setIconSize(QtCore.QSize(40, 40))
        self.send_btn.setObjectName("toolButton")
        self.online = QtWidgets.QLabel(self.page_2)
        self.online.setGeometry(QtCore.QRect(0, 0, 391, 71))
        self.online.setStyleSheet("background-color: rgb(3, 49, 75);\n"
                                  "font: 10pt \"MS Shell Dlg 2\";"
                                  "color: rgb(130, 130, 130);")
        self.online.setObjectName("label_4")
        self.online.setAlignment(QtCore.Qt.AlignCenter)
        self.left_btn = QtWidgets.QToolButton(self.page_2)
        self.left_btn.setGeometry(QtCore.QRect(390, 0, 61, 71))
        self.left_btn.setStyleSheet("background-color: rgb(3, 49, 75);")
        self.left_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("custom_qt_classes/img_source/left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.left_btn.setIcon(icon1)
        self.left_btn.setIconSize(QtCore.QSize(30, 30))
        self.left_btn.setObjectName("toolButton_2")
        self.msg_txt_edit = QtWidgets.QTextEdit(self.page_2)
        self.msg_txt_edit.setGeometry(QtCore.QRect(0, 850, 401, 51))
        self.msg_txt_edit.setStyleSheet("background-color: rgb(88, 172, 174);\n"
                                        "font: 10pt \"MS Shell Dlg 2\";")
        self.msg_txt_edit.setObjectName("textEdit")
        self.label_3.raise_()
        self.listWidget.raise_()
        self.send_btn.raise_()
        self.online.raise_()
        self.left_btn.raise_()
        self.msg_txt_edit.raise_()
        self.stackedWidget.addWidget(self.page_2)
        self.close_btn = QtWidgets.QPushButton(Form)
        self.close_btn.setGeometry(QtCore.QRect(400, 0, 51, 41))
        self.close_btn.setStyleSheet("background-color: rgb(1, 14, 30);\n"
                                     "color: rgb(130, 130, 130);\n"
                                     "font: 12pt \"MS Shell Dlg 2\";")
        self.close_btn.setObjectName("close_btn")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(0, -5, 451, 51))
        self.label_5.setStyleSheet("background-color: rgb(1, 14, 30);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_5.raise_()
        self.stackedWidget.raise_()
        self.close_btn.raise_()

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.username_btn.setText(_translate("Form", "next"))
        self.label.setText(_translate("Form",
                                      "<html><head/><body><p><span style=\" font-size:14pt; color:#000000;\">please enter your name</span></p></body></html>"))
        self.cancel_btn.setText(_translate("Form", "cancel"))
        self.close_btn.setText(_translate("Form", "x"))
