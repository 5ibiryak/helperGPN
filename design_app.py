# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_5.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from random import randint
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
) 




class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Settings_window=Ui_Settings()
        self.logic=True

    def show_new_window(self, checked):
        print('AA')
        logic=False
        return logic
        
 
     
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(803, 733)
        MainWindow.setStyleSheet("")
        MainWindow.setAnimated(True)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
"    \n"
"    background-color: rgb(57, 131, 177);\n"
"}\n"
"\n"
"QPushButton{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    border: 1px solid white\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 570, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(True)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(79, 158, 218);\n"
"}")
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setObjectName("pushButton")
        self.textBrowser_object = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_object.setGeometry(QtCore.QRect(240, 230, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.textBrowser_object.setFont(font)
        self.textBrowser_object.setStyleSheet("QTextBrowser{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    border: 0px\n"
"}")
        self.textBrowser_object.setObjectName("textBrowser_object")
        self.textBrowser_data = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_data.setGeometry(QtCore.QRect(240, 320, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.textBrowser_data.setFont(font)
        self.textBrowser_data.setStyleSheet("QTextBrowser{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    border: 0px\n"
"}")
        self.textBrowser_data.setObjectName("textBrowser_data")
        self.textEdit_object = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_object.setGeometry(QtCore.QRect(240, 270, 321, 31))
        self.textEdit_object.setStyleSheet("QTextEdit{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}")
        self.textEdit_object.setObjectName("textEdit_object")
        self.textBrowser_folder = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_folder.setGeometry(QtCore.QRect(240, 50, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.textBrowser_folder.setFont(font)
        self.textBrowser_folder.setStyleSheet("QTextBrowser{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    border: 0px\n"
"}")
        self.textBrowser_folder.setObjectName("textBrowser_folder")
        self.textBrowser_excel = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_excel.setGeometry(QtCore.QRect(240, 140, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.textBrowser_excel.setFont(font)
        self.textBrowser_excel.setStyleSheet("QTextBrowser{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    border: 0px\n"
"}")
        self.textBrowser_excel.setObjectName("textBrowser_excel")
        self.pushButton_folder = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_folder.setGeometry(QtCore.QRect(580, 90, 31, 31))
        self.pushButton_folder.setStyleSheet("QPushButton{\n"
"    background-color: rgb(79, 158, 218);\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_folder.setObjectName("pushButton_folder")
        self.pushButton_excel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_excel.setGeometry(QtCore.QRect(580, 180, 31, 31))
        self.pushButton_excel.setStyleSheet("QPushButton{\n"
"    background-color: rgb(79, 158, 218);\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_excel.setObjectName("pushButton_excel")
        self.plainTextEdit_folder = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_folder.setGeometry(QtCore.QRect(240, 90, 321, 31))
        self.plainTextEdit_folder.setStyleSheet("QPlainTextEdit{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}")
        self.plainTextEdit_folder.setObjectName("plainTextEdit_folder")
        self.plainTextEdit_excel = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_excel.setGeometry(QtCore.QRect(240, 180, 321, 31))
        self.plainTextEdit_excel.setStyleSheet("QPlainTextEdit{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}")
        self.plainTextEdit_excel.setObjectName("plainTextEdit_excel")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(240, 510, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("QCheckBox{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.checkBox.setObjectName("checkBox")
        self.textBrowser_data_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_data_2.setGeometry(QtCore.QRect(240, 410, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.textBrowser_data_2.setFont(font)
        self.textBrowser_data_2.setStyleSheet("QTextBrowser{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    border: 0px\n"
"}")
        self.textBrowser_data_2.setObjectName("textBrowser_data_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.addItems(["Agisoft Metashape","Contex capture","Pix4D"])
        self.comboBox.setGeometry(QtCore.QRect(240, 450, 321, 31))
        self.comboBox.setAutoFillBackground(True)
        self.comboBox.setStyleSheet("QComboBox{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QComboBox::down-button{\n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(240, 360, 321, 31))
        self.dateEdit.setStyleSheet("QDateEdit{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QDateEdit::down-button{\n"
"\n"
"    \n"
"}\n"
"\n"
"QDateEdit::up-button{\n"
"    \n"
"\n"
"}")

                
        self.dateEdit.setWrapping(False)
        self.dateEdit.setFrame(True)
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setReadOnly(False)
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEdit.setSpecialValueText("")
        self.dateEdit.setAccelerated(False)
        self.dateEdit.setKeyboardTracking(True)
        self.dateEdit.setProperty("showGroupSeparator", False)
        self.dateEdit.setObjectName("dateEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction()
        self.actionSettings.setObjectName("actionSettings")
        ###########

        self.actionSettings.triggered.connect(self.show_new_window)

        ###########
        self.actionInfromation = QtWidgets.QAction(MainWindow)
        self.actionInfromation.setObjectName("actionInfromation")
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionInfromation)
        self.menubar.addAction(self.menuFile.menuAction())

        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Создать"))
        self.textBrowser_object.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Rockwell\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Введите объект</span></p></body></html>"))
        self.textBrowser_data.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Rockwell\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Введите дату</span></p></body></html>"))
        self.textBrowser_folder.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Rockwell\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Выберите папку</span></p></body></html>"))
        self.textBrowser_excel.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Rockwell\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Выберите документ excel</span></p></body></html>"))
        self.pushButton_folder.setText(_translate("MainWindow", "..."))
        self.pushButton_excel.setText(_translate("MainWindow", "..."))
        self.checkBox.setText(_translate("MainWindow", "Добавить id"))
        self.textBrowser_data_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Rockwell\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Выберите программу</span></p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionInfromation.setText(_translate("MainWindow", "Infromation"))



class Ui_Settings(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)
        print('check 2')

    def setupUi(self, Settings):
        print("GOOD")
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
