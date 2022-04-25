from asyncio import open_connection
from inspect import isabstract
from sqlite3 import Time, connect
from typing_extensions import Self
from unittest import signals
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer, QRect
import PySide2
from menu_start import Ui_AliasGameMenuClass # menu start 
from grupa_start import Ui_TeamNameClass # grupa start
from rules_knoner import Ui_RulesTextClass #rules kanoner
from text_start import Ui_TextNameClass # game text
from winner import Ui_WinnerTeamClass # game winner
import time
import random
import sys
from ast import arg
import imp
import threading

class Game_Start:
    def openMenu(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.AliasGameMenuClass = QtWidgets.QWidget()
        self.ui = Ui_AliasGameMenuClass()
        self.ui.setupUi(self.AliasGameMenuClass)
        self.AliasGameMenuClass.show()

    def openNewGameWindow(self):
        self.TeamNameClass # anpayman global ara vor ashxati
        self.TeamNameClass = QtWidgets.QWidget()
        self.ui = self.Ui_TeamNameClass()
        self.ui.setupUi(self.TeamNameClass)
        self.AliasGameMenuClass.hide()  # kame close()
        self.TeamNameClass.show()

        def returnToNewGame():
            self.TeamNameClass.close() #het em galic back em anum
            self.AliasGameMenuClass.show()

        self.ui.btn_back.clicked.connect(returnToNewGame) # baci hamara

        self.ui.btn_plainTextEdit1.setPlaceholderText("Enter Your Team!")
        self.ui.btn_plainTextEdit_2.setPlaceholderText("Enter Your Team!")

st = Game_Start()
st.openMenu()
st.openNewGameWindow()