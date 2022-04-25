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

app = QtWidgets.QApplication(sys.argv)

AliasGameMenuClass = QtWidgets.QWidget()
ui = Ui_AliasGameMenuClass()
ui.setupUi(AliasGameMenuClass)
AliasGameMenuClass.show()

# team name string
team1 = ""
team2 = ""
start_team = ""
points_team1 = 0
points_team2 = 0
total_results = {}
res1 = 0
res2 = 0
stop_game = False
start_second = False
isStart = False
startTime = 0
second = 1000
words = ["մաչո","ակումուլյատոր","լեքսիկոն","պարոդիա","մկկալ","բլբլալ","բոռալ","կենդանի"
        ,"հով","շլոփա","մորուք","սկեսուր","թպրտալ","ոռնալ","որթ"]

# .......................................


# logic...
def openNewGameWindow(): #bacum em errkrod patuhans
    global TeamNameClass # anpayman global ara vor ashxati
    TeamNameClass = QtWidgets.QWidget()
    ui = Ui_TeamNameClass()
    ui.setupUi(TeamNameClass)
    AliasGameMenuClass.hide()  # kame close()
    TeamNameClass.show() # show cuyc talu hamara

    def returnToNewGame():
        TeamNameClass.close() #het em galic back em anum
        AliasGameMenuClass.show()

    ui.btn_back.clicked.connect(returnToNewGame) # baci hamara

    ui.btn_plainTextEdit1.setPlaceholderText("Enter Your Team!")
    ui.btn_plainTextEdit_2.setPlaceholderText("Enter Your Team!")
    
    

    def get_text_team1():
        global team1,team2
        team1 = ui.btn_plainTextEdit1.toPlainText()
        print("Team1: ",team1)
    
    def get_text_team2():
        global team1,team2
        team2 = ui.btn_plainTextEdit_2.toPlainText()
        print("Team2: ",team2)

    ui.btn_team1.clicked.connect(get_text_team1)
    ui.btn_team2.clicked.connect(get_text_team2)

    

    def openStartGame():
        global TextNameClass
        TextNameClass = QtWidgets.QWidget()
        ui = Ui_TextNameClass()
        ui.setupUi(TextNameClass)
        TeamNameClass.hide()
        TextNameClass.show()
        

        

        def game_stop():
            stop_game = True
            if stop_game == True:
                sys.exit(app.exec_())
                
        
        ui.btn_stop.clicked.connect(game_stop)

        
        def time_start():
            global isStart,startTime
            isStart = True
            startTime = time.time()
            
        
        def reset():
            global isStart
            isStart = False

            
        
        ui.push_start.clicked.connect(time_start)
        ui.push_reset.clicked.connect(reset)

        def timerFunction():
            global isStart,startTime
            if isStart:
                timer_r = int(time.time() - startTime)

                hours = timer_r // 3600
                minuts = (timer_r % 3600) // 60
                second = timer_r % 60
                #print(second)

                if second > 60:
                    isStart = False
                else:
                    hours = str(hours);minuts = str(minuts); second = str(second)

                    time_str = '0'*(2-len(hours))+hours+':'+'0'*(2-len(minuts))+minuts+':'+'0'*(2-len(second))+second 
                    ui.btn_second.setText(time_str)



        timer = QtCore.QTimer(TextNameClass)
        timer.timeout.connect(timerFunction)
        timer.start(1000)




        def returnRandomTextTeam1():
            global points_team1
            global total_results
            
            print("Started " + team1 + " good time!", " and your points: ",points_team1)
            
            points_team1 = 0
            ui.btn_text1.setCheckable(True)
            ui.btn_text2.setCheckable(True)
            ui.btn_text3.setCheckable(True)
            ui.btn_text4.setCheckable(True)
            ui.btn_text5.setCheckable(True)
            ui.btn_text6.setCheckable(True)
            ui.btn_text7.setCheckable(True)

            ui.btn_text1.setText(words[0])
            if ui.btn_text1.isChecked():
                points_team1 += 7
            ui.btn_text2.setText(words[1])
            if ui.btn_text2.isChecked():
                points_team1 += 7
            ui.btn_text3.setText(words[2])
            if ui.btn_text3.isChecked():
                points_team1 += 7
            ui.btn_text4.setText(words[3])
            if ui.btn_text4.isChecked():
                points_team1 += 7
            ui.btn_text5.setText(words[4])
            if ui.btn_text5.isChecked():
                points_team1 += 7
            ui.btn_text6.setText(words[5])
            if ui.btn_text6.isChecked():
                points_team1 += 7
            ui.btn_text7.setText(words[6])
            if ui.btn_text7.isChecked():
                points_team1 += 7

            
            res1 = points_team1
            total_results[team1] = res1
            print(total_results.items())

            ui.btn_text1.clicked.connect(returnRandomTextTeam1)
            ui.btn_text2.clicked.connect(returnRandomTextTeam1)
            ui.btn_text3.clicked.connect(returnRandomTextTeam1)
            ui.btn_text4.clicked.connect(returnRandomTextTeam1)
            ui.btn_text5.clicked.connect(returnRandomTextTeam1)
            ui.btn_text6.clicked.connect(returnRandomTextTeam1)
            ui.btn_text7.clicked.connect(returnRandomTextTeam1)


        

        def openStartTema2():
            global TextNameClass
            TextNameClass = QtWidgets.QWidget()
            ui = Ui_TextNameClass()
            ui.setupUi(TextNameClass)
            AliasGameMenuClass.close()
            TextNameClass.show()

            def game_stop():
                stop_game = True
                if stop_game == True:
                    sys.exit(app.exec_())
                
        
            ui.btn_stop.clicked.connect(game_stop)

            def time_start():
                global isStart,startTime
                isStart = True
                startTime = time.time()
                
        
            def reset():
                global isStart
                isStart = False

        
            ui.push_start.clicked.connect(time_start)
            ui.push_reset.clicked.connect(reset)

            def timerFunction():
                global isStart,startTime
                if isStart:
                    timer_r = int(time.time() - startTime)

                    hours = timer_r // 3600
                    minuts = (timer_r % 3600) // 60
                    second = timer_r % 60

                    if second > 60:
                        isStart = False
                    else:
                        hours = str(hours);minuts = str(minuts); second = str(second)

                        time_str = '0'*(2-len(hours))+hours+':'+'0'*(2-len(minuts))+minuts+':'+'0'*(2-len(second))+second 
                        ui.btn_second.setText(time_str)



            timer = QtCore.QTimer(TextNameClass)
            timer.timeout.connect(timerFunction)
            timer.start(1000)



            def goToWinnerTeam():
                global WinnerTeamClass
                WinnerTeamClass = QtWidgets.QWidget()
                ui = Ui_WinnerTeamClass()
                ui.setupUi(WinnerTeamClass)
                TeamNameClass.close()
                TextNameClass.close()
                WinnerTeamClass.show()
                        
                print("Resulttt",total_results.items())

                def returnWinnerTeam():
                    global points_team1,points_team2
                    global res1,res2
                    print(res1,res2)
                    print(points_team1,points_team2)
                    if points_team1 > points_team2:
                        ui.winner_team.setText("Win "+team1)
                    elif points_team1 < points_team2:
                        ui.winner_team.setText("Win "+team2)
                    else:
                        ui.winner_team.setText("Equal")
                returnWinnerTeam()
            ui.push_next.clicked.connect(goToWinnerTeam)


            def teamtwologic():
                global points_team2
                global res1,res2
                global total_results
                print("Started " + team2 + " good time! ","and your points: ",points_team2)
                
                points_team2 = 0
                ui.btn_text1.setCheckable(True)
                ui.btn_text2.setCheckable(True)
                ui.btn_text3.setCheckable(True)
                ui.btn_text4.setCheckable(True)
                ui.btn_text5.setCheckable(True)
                ui.btn_text6.setCheckable(True)
                ui.btn_text7.setCheckable(True)

                ui.btn_text1.setText(words[7])
                if ui.btn_text1.isChecked():
                    points_team2 += 7
                ui.btn_text2.setText(words[8])
                if ui.btn_text2.isChecked():
                    points_team2 += 7
                ui.btn_text3.setText(words[9])
                if ui.btn_text3.isChecked():
                    points_team2 += 7
                ui.btn_text4.setText(words[10])
                if ui.btn_text4.isChecked():
                    points_team2 += 7
                ui.btn_text5.setText(words[11])
                if ui.btn_text5.isChecked():
                    points_team2 += 7
                ui.btn_text6.setText(words[12])
                if ui.btn_text6.isChecked():
                    points_team2 += 7
                ui.btn_text7.setText(words[13])
                if ui.btn_text7.isChecked():
                    points_team2 += 7


                res2 = points_team2
                total_results[team2] = res2
                print(total_results.items())
                
                ui.btn_text1.clicked.connect(teamtwologic)
                ui.btn_text2.clicked.connect(teamtwologic)
                ui.btn_text3.clicked.connect(teamtwologic)
                ui.btn_text4.clicked.connect(teamtwologic)
                ui.btn_text5.clicked.connect(teamtwologic)
                ui.btn_text6.clicked.connect(teamtwologic)
                ui.btn_text7.clicked.connect(teamtwologic)
            
            teamtwologic()

        ui.push_team2.clicked.connect(openStartTema2)
        
        returnRandomTextTeam1()
        
        

        def goToWinnerTeam():
            global WinnerTeamClass
            WinnerTeamClass = QtWidgets.QWidget()
            ui = Ui_WinnerTeamClass()
            ui.setupUi(WinnerTeamClass)
            TeamNameClass.close()
            TextNameClass.close()
            WinnerTeamClass.show()
                    
            print("Resulttt",total_results.items())

            def returnWinnerTeam():
                global points_team1,points_team2
                global res1,res2
                print(res1,res2)
                print(points_team1,points_team2)
                if points_team1 > points_team2:
                    ui.winner_team.setText("Win "+team1)
                elif points_team1 < points_team2:
                    ui.winner_team.setText("Win "+team2)
                else:
                    ui.winner_team.setText("Equal")
            returnWinnerTeam()



            
        
        ui.push_next.clicked.connect(goToWinnerTeam)
        
        
    
    ui.btn_StartGame.clicked.connect(openStartGame)

ui.btn_NewGame.clicked.connect(openNewGameWindow) # newgame buttnem ashxtacnum 





def openRules():
    global RulesTextClass
    RulesTextClass = QtWidgets.QWidget()
    ui = Ui_RulesTextClass()
    ui.setupUi(RulesTextClass)
    RulesTextClass.show()

    def returnToMenu():
        RulesTextClass.close()
        AliasGameMenuClass.show()

    ui.btn_back_rules.clicked.connect(returnToMenu)

ui.btn_Rules.clicked.connect(openRules)



sys.exit(app.exec_())