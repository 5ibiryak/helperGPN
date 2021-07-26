from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from project_1 import Ui_MainWindow
from tkinter import *
import os
from openpyxl import load_workbook
 
root = Tk()
myFileName = "list_of_flights.xlsx"

def btn_click():
    name = ui.textEdit_object.toPlainText()
    date = ui.textEdit_data.toPlainText()
    os.chdir('D:/CT_BAS')
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
    os.chdir('D:/CT_BAS')
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

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

ui.pushButton.clicked.connect(btn_click)

sys.exit(app.exec_())