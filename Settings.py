from Settings_design import Ui_Settings
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

### имена должны отображаться в окне


myFileName = ""
dirlist=' d'


### вывод занесенных значений
def string_1():
    try:
        with open("path.txt","r",encoding="utf8") as file:
            contents = file.readlines()
            str1 = contents[0]
            return str1
    except:
        none=''
        return none
def string_2():
    try:
        with open("path.txt","r",encoding="utf8") as file:
            contents = file.readlines()
            str2 = contents[1]
            return str2
    except:
        none=''
        return none
def string_3():
    try:
        with open("path.txt","r",encoding="utf8") as file:
            contents = file.readlines()
            str3 = contents[2]
            return str3
    except:
        none=''
        return none

def getFileName_1():
    filename_1,_ = QtWidgets.QFileDialog.getOpenFileName()
    global myFileName_1
    myFileName_1 = filename_1
    ui.plainTextEdit_folder.appendHtml(format(filename_1))

    
    
def getFileName_2():
    filename,_ = QtWidgets.QFileDialog.getOpenFileName()
    global myFileName_2
    myFileName_2 = filename
    ui.plainTextEdit_folder_2.appendHtml(format(filename))

    

def getFileName_3():
    filename,_ = QtWidgets.QFileDialog.getOpenFileName()
    global myFileName_3
    myFileName_3 = filename
    ui.plainTextEdit_folder_3.appendHtml(format(filename))

    


def save():
    try:
        with open("path.txt", "w",encoding="utf8") as file:
            file.write(myFileName_1+'\n')
            file.write(myFileName_2+'\n')
            file.write(myFileName_3)
    except:
        pass
        


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_Settings()
ui.setupUi(MainWindow)
MainWindow.show()


ui.plainTextEdit_folder.appendHtml(format(string_1()))
ui.plainTextEdit_folder_2.appendHtml(format(string_2()))
ui.plainTextEdit_folder_3.appendHtml(format(string_3()))



ui.pushButton_folder.clicked.connect(getFileName_1)
ui.pushButton_folder_2.clicked.connect(getFileName_2)
ui.pushButton_folder_3.clicked.connect(getFileName_3)
ui.pushButton.clicked.connect(save)

sys.exit(app.exec_())