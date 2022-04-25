

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RulesTextClass(object):
    def setupUi(self, RulesTextClass):
        RulesTextClass.setObjectName("RulesTextClass")
        RulesTextClass.resize(400, 289)
        RulesTextClass.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_Rules_lable = QtWidgets.QTextBrowser(RulesTextClass)
        self.btn_Rules_lable.setGeometry(QtCore.QRect(5, 11, 391, 221))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.btn_Rules_lable.setFont(font)
        self.btn_Rules_lable.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.btn_Rules_lable.setObjectName("btn_Rules_lable")
        self.btn_back_rules = QtWidgets.QPushButton(RulesTextClass)
        self.btn_back_rules.setGeometry(QtCore.QRect(300, 240, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.btn_back_rules.setFont(font)
        self.btn_back_rules.setStyleSheet("background-color: rgb(245, 121, 0);")
        self.btn_back_rules.setObjectName("btn_back_rules")

        self.retranslateUi(RulesTextClass)
        QtCore.QMetaObject.connectSlotsByName(RulesTextClass)

    def retranslateUi(self, RulesTextClass):
        _translate = QtCore.QCoreApplication.translate
        RulesTextClass.setWindowTitle(_translate("RulesTextClass", "AliasArmenianGame"))
        self.btn_Rules_lable.setHtml(_translate("RulesTextClass", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%; background-color:transparent;\"><span style=\" font-family:\'Roboto Condensed\',\'sans-serif\'; font-weight:400; color:#333333;\">Alias ​​սեղանի խաղի կանոնները</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%; background-color:transparent;\"><span style=\" font-family:\'Roboto Condensed\',\'sans-serif\'; font-weight:400; color:#333333;\">Խաղացողները բաժանվում են թիմերի (երկու հոգուց), որոշում են հերթականությունը, թիմում պայմանավորվում են, թե ով է բացատրելու և ով կընկալի, որոշում են քարտերի բառերի թիվը, դնում են ավազի ժամացույց և փորձում են մեկ րոպե հասկանալ միմյանց։</span></p></body></html>"))
        self.btn_back_rules.setText(_translate("RulesTextClass", "Back"))
