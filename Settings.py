from Settings_design import Ui_Settings
from PyQt5 import QtCore, QtGui, QtWidgets
import sys



myFileName = ""



def getFileName():
    filename,_ = QtWidgets.QFileDialog.getOpenFileName()
    global myFileName
    myFileName = filename
    ui.plainTextEdit_folder.appendHtml(format(filename))
    ui.plainTextEdit_folder.setGeometry(QtCore.QRect(120, 70, 321, 46))

def getFileName2():
    filename,_ = QtWidgets.QFileDialog.getOpenFileName()
    global myFileName
    myFileName = filename
    ui.plainTextEdit_folder_2.appendHtml(format(filename))
    ui.plainTextEdit_folder_2.setGeometry(QtCore.QRect(120, 170, 321, 46))

def getFileName3():
    filename,_ = QtWidgets.QFileDialog.getOpenFileName()
    global myFileName
    myFileName = filename
    ui.plainTextEdit_folder_3.appendHtml(format(filename))
    ui.plainTextEdit_folder_3.setGeometry(QtCore.QRect(120, 270, 321, 46))


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_Settings()
ui.setupUi(MainWindow)
MainWindow.show()




ui.pushButton_folder.clicked.connect(getFileName)
ui.pushButton_folder_2.clicked.connect(getFileName2)
ui.pushButton_folder_3.clicked.connect(getFileName3)


sys.exit(app.exec_())