
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TeamNameClass(object):
    def setupUi(self, TeamNameClass):
        TeamNameClass.setObjectName("TeamNameClass")
        TeamNameClass.resize(533, 346)
        TeamNameClass.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_team1 = QtWidgets.QPushButton(TeamNameClass)
        self.btn_team1.setGeometry(QtCore.QRect(10, 20, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        self.btn_team1.setFont(font)
        self.btn_team1.setStyleSheet("background-color: rgb(245, 121, 0);\n"
"color: rgb(46, 52, 54);")
        self.btn_team1.setObjectName("btn_team1")
        self.btn_team2 = QtWidgets.QPushButton(TeamNameClass)
        self.btn_team2.setGeometry(QtCore.QRect(10, 120, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        self.btn_team2.setFont(font)
        self.btn_team2.setStyleSheet("background-color: rgb(245, 121, 0);\n"
"color: rgb(46, 52, 54);")
        self.btn_team2.setObjectName("btn_team2")
        #self.btn_plainTextEdit1 = QtWidgets.QPlainTextEdit(TeamNameClass)
        self.btn_plainTextEdit1 = QtWidgets.QTextEdit(TeamNameClass)
        self.btn_plainTextEdit1.setGeometry(QtCore.QRect(280, 20, 241, 70))
        self.btn_plainTextEdit1.setObjectName("btn_plainTextEdit1")
        #self.btn_plainTextEdit_2 = QtWidgets.QPlainTextEdit(TeamNameClass)
        self.btn_plainTextEdit_2 = QtWidgets.QTextEdit(TeamNameClass)
        self.btn_plainTextEdit_2.setGeometry(QtCore.QRect(280, 120, 241, 70))
        self.btn_plainTextEdit_2.setObjectName("btn_plainTextEdit_2")
        self.btn_StartGame = QtWidgets.QPushButton(TeamNameClass)
        self.btn_StartGame.setGeometry(QtCore.QRect(10, 210, 511, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn_StartGame.setFont(font)
        self.btn_StartGame.setStyleSheet("background-color: rgb(245, 121, 0);\n"
"color: rgb(46, 52, 54);")
        self.btn_StartGame.setObjectName("btn_StartGame")
        self.btn_back = QtWidgets.QPushButton(TeamNameClass)
        self.btn_back.setGeometry(QtCore.QRect(430, 310, 89, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet("background-color: rgb(245, 121, 0);\n"
"color: rgb(46, 52, 54);")
        self.btn_back.setObjectName("btn_back")

        self.retranslateUi(TeamNameClass)
        self.btn_team1.clicked.connect(TeamNameClass.show)
        self.btn_team2.clicked.connect(TeamNameClass.show)
        QtCore.QMetaObject.connectSlotsByName(TeamNameClass)

    def retranslateUi(self, TeamNameClass):
        _translate = QtCore.QCoreApplication.translate
        TeamNameClass.setWindowTitle(_translate("TeamNameClass", "AliasArmenianGame"))
        self.btn_team1.setText(_translate("TeamNameClass", "Team 1"))
        self.btn_team2.setText(_translate("TeamNameClass", "Team 2"))
        self.btn_StartGame.setText(_translate("TeamNameClass", "Start Game"))
        self.btn_back.setText(_translate("TeamNameClass", "Back"))
