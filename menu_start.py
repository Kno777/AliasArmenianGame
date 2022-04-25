
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AliasGameMenuClass(object):
    def setupUi(self, AliasGameMenuClass):
        AliasGameMenuClass.setObjectName("AliasGameMenuClass")
        AliasGameMenuClass.resize(570, 341)
        AliasGameMenuClass.setStyleSheet("background-color: rgb(114, 159, 207);\n"
"background-color: rgb(238, 238, 236);")
        self.label_logo_alias = QtWidgets.QLabel(AliasGameMenuClass)
        self.label_logo_alias.setGeometry(QtCore.QRect(30, 0, 561, 201))
        self.label_logo_alias.setText("")
        self.label_logo_alias.setPixmap(QtGui.QPixmap("unnamed.png"))
        self.label_logo_alias.setObjectName("label_logo_alias")
        self.btn_NewGame = QtWidgets.QPushButton(AliasGameMenuClass)
        self.btn_NewGame.setGeometry(QtCore.QRect(30, 210, 511, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn_NewGame.setFont(font)
        self.btn_NewGame.setStyleSheet("background-color: rgb(245, 121, 0);\n"
"color: rgb(46, 52, 54);")
        self.btn_NewGame.setObjectName("btn_NewGame")
        self.btn_Rules = QtWidgets.QPushButton(AliasGameMenuClass)
        self.btn_Rules.setGeometry(QtCore.QRect(30, 270, 511, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn_Rules.setFont(font)
        self.btn_Rules.setStyleSheet("background-color: rgb(245, 121, 0);\n"
"color: rgb(46, 52, 54);")
        self.btn_Rules.setObjectName("btn_Rules")

        self.retranslateUi(AliasGameMenuClass)
        QtCore.QMetaObject.connectSlotsByName(AliasGameMenuClass)

    def retranslateUi(self, AliasGameMenuClass):
        _translate = QtCore.QCoreApplication.translate
        AliasGameMenuClass.setWindowTitle(_translate("AliasGameMenuClass", "AliasArmenianGame"))
        self.btn_NewGame.setText(_translate("AliasGameMenuClass", "New Game"))
        self.btn_Rules.setText(_translate("AliasGameMenuClass", "Rules"))

