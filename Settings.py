# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Settings.ui'
#



from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(560, 490)
        Settings.setStyleSheet("QMainWindow{\n"
"    \n"
"}")
        self.centralwidget = QtWidgets.QWidget(Settings)
        self.centralwidget.setStyleSheet("QWidget{\n"
"    \n"
"    background-color: rgb(57, 131, 177);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    border: 1px solid white\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit_folder = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_folder.setGeometry(QtCore.QRect(120, 90, 321, 31))
        self.plainTextEdit_folder.setStyleSheet("QPlainTextEdit{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}")
        self.plainTextEdit_folder.setObjectName("plainTextEdit_folder")
        self.textBrowser_folder = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_folder.setGeometry(QtCore.QRect(120, 40, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.textBrowser_folder.setFont(font)
        self.textBrowser_folder.setStyleSheet("QTextBrowser{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    border: 0px\n"
"}")
        self.textBrowser_folder.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_folder.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_folder.setObjectName("textBrowser_folder")
        self.textBrowser_folder_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_folder_2.setGeometry(QtCore.QRect(120, 140, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.textBrowser_folder_2.setFont(font)
        self.textBrowser_folder_2.setStyleSheet("QTextBrowser{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    border: 0px\n"
"}")
        self.textBrowser_folder_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_folder_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_folder_2.setObjectName("textBrowser_folder_2")
        self.plainTextEdit_folder_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_folder_2.setGeometry(QtCore.QRect(120, 190, 321, 31))
        self.plainTextEdit_folder_2.setStyleSheet("QPlainTextEdit{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}")
        self.plainTextEdit_folder_2.setObjectName("plainTextEdit_folder_2")
        self.plainTextEdit_folder_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_folder_3.setGeometry(QtCore.QRect(120, 290, 321, 31))
        self.plainTextEdit_folder_3.setStyleSheet("QPlainTextEdit{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}")
        self.plainTextEdit_folder_3.setObjectName("plainTextEdit_folder_3")
        self.textBrowser_folder_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_folder_3.setGeometry(QtCore.QRect(120, 240, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.textBrowser_folder_3.setFont(font)
        self.textBrowser_folder_3.setStyleSheet("QTextBrowser{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    border: 0px\n"
"}")
        self.textBrowser_folder_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_folder_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_folder_3.setObjectName("textBrowser_folder_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 350, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(True)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(79, 158, 218);\n"
"    border-radius: 5px;\n"
"}")
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_folder = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_folder.setGeometry(QtCore.QRect(460, 90, 31, 31))
        self.pushButton_folder.setStyleSheet("QPushButton{\n"
"    background-color: rgb(79, 158, 218);\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_folder.setObjectName("pushButton_folder")
        self.pushButton_folder_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_folder_2.setGeometry(QtCore.QRect(460, 190, 31, 31))
        self.pushButton_folder_2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(79, 158, 218);\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_folder_2.setObjectName("pushButton_folder_2")
        self.pushButton_folder_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_folder_3.setGeometry(QtCore.QRect(460, 290, 31, 31))
        self.pushButton_folder_3.setStyleSheet("QPushButton{\n"
"    background-color: rgb(79, 158, 218);\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_folder_3.setObjectName("pushButton_folder_3")
        Settings.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Settings)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 26))
        self.menubar.setObjectName("menubar")
        Settings.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Settings)
        self.statusbar.setObjectName("statusbar")
        Settings.setStatusBar(self.statusbar)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "MainWindow"))
        self.textBrowser_folder.setHtml(_translate("Settings", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Rockwell\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Расположение  Agisoft MS</p></body></html>"))
        self.textBrowser_folder_2.setHtml(_translate("Settings", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Rockwell\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Расположение  Contex Capture</p></body></html>"))
        self.textBrowser_folder_3.setHtml(_translate("Settings", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Rockwell\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Расположение  Pix4D</p></body></html>"))
        self.pushButton.setText(_translate("Settings", "Сохранить"))
        self.pushButton_folder.setText(_translate("Settings", "..."))
        self.pushButton_folder_2.setText(_translate("Settings", "..."))
        self.pushButton_folder_3.setText(_translate("Settings", "..."))
