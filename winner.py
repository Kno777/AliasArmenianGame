
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WinnerTeamClass(object):
    def setupUi(self, WinnerTeamClass):
        WinnerTeamClass.setObjectName("WinnerTeamClass")
        WinnerTeamClass.resize(520, 263)
        WinnerTeamClass.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.label_potho_winner = QtWidgets.QLabel(WinnerTeamClass)
        self.label_potho_winner.setGeometry(QtCore.QRect(20, 10, 511, 181))
        self.label_potho_winner.setText("")
        self.label_potho_winner.setPixmap(QtGui.QPixmap("winner.jpg"))
        self.label_potho_winner.setObjectName("label_potho_winner")
        self.winner_team = QtWidgets.QLineEdit(WinnerTeamClass)
        self.winner_team.setGeometry(QtCore.QRect(170, 200, 190, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.winner_team.setFont(font)
        self.winner_team.setStyleSheet("background-color: rgb(245, 121, 0);")
        self.winner_team.setObjectName("winner_team")

        self.retranslateUi(WinnerTeamClass)
        QtCore.QMetaObject.connectSlotsByName(WinnerTeamClass)

    def retranslateUi(self, WinnerTeamClass):
        _translate = QtCore.QCoreApplication.translate
        WinnerTeamClass.setWindowTitle(_translate("WinnerTeamClass", "AliasArmenianGame"))
        self.winner_team.setText(_translate("WinnerTeamClass", "       Team 1"))
