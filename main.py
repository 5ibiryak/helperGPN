from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from project_2 import Ui_MainWindow
from tkinter import *
import os
from openpyxl import load_workbook
 
dirlist = 'D:/'
myFileName = "list_of_flights.xlsx"

def btn_click():
    name = ui.textEdit_object.toPlainText()
    date = ui.textEdit_data.toPlainText()
    dirlist = ui.plainTextEdit_folder.toPlainText()
    os.chdir(dirlist)
    #создание главной папки
    os.mkdir(name + '_' + date)
    os.chdir(name + '_' + date)
    #создание подпапок в главной
    os.mkdir("Field")
    os.mkdir("P4D_processing")
    os.mkdir('Results' + '_' + name + '_' + date)
    #создание папок в P4D_processing
    os.chdir('P4D_processing')
    os.mkdir(name + '_' + date)
    #создание папок в Results
    os.chdir("..")
    os.chdir('Results' + '_' + name + '_' + date)
    os.mkdir('DEM')
    os.mkdir('Ortho')
    os.mkdir('Point_cloud')
    print('Hello')
    
    # добавление записи о полете в таблицу
    os.chdir(dirlist)
    wb = load_workbook(myFileName)
    ws = wb.worksheets[0]
    name = name+''
    date = date+''
    # проверка не пуста ли переменная имя
    if name:
        newItemID = ws.max_row
        ws.append([newItemID, name, date])
    else:
        print('No name entered')
    #завершение работы с таблицой
    wb.save(filename=myFileName)
    wb.close()
    
#выбор папки
def getDirectory():
    dirlist = QtWidgets.QFileDialog.getExistingDirectory()
    ui.plainTextEdit_folder.setPlainText(format(dirlist))
    ui.plainTextEdit_folder.setGeometry(QtCore.QRect(240, 90, 321, 46))

#выбор файла
def getFileName():
        filename = QtWidgets.QFileDialog.getOpenFileName()
        ui.plainTextEdit_excel.appendHtml(format(filename))
        ui.plainTextEdit_excel.setGeometry(QtCore.QRect(240, 180, 321, 46))

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

ui.plainTextEdit_folder.appendHtml(format(dirlist))

ui.pushButton_folder.clicked.connect(getDirectory)
ui.pushButton_excel.clicked.connect(getFileName)
ui.pushButton.clicked.connect(btn_click)

sys.exit(app.exec_())
