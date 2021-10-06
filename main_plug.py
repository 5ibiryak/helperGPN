import metashape as Metashape
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from design_plug import Ui_MainWindow
import sys
from glob import glob
from PyQt5 import sip
import os

# Checking compatibility
# compatible_major_version = "1.7"
# found_major_version = ".".join(Metashape.app.version.split('.')[:2])
# if found_major_version != compatible_major_version:
#     raise Exception("Incompatible Metashape version: {} != {}".format(found_major_version, compatible_major_version))

myLogText = "" # строка для логов

#кнопка split_by_cameras
def btn_split():
    global mychunk
    mychunk.matchPhotos(downscale=1, generic_preselection=True, reference_preselection=False)
    mychunk.alignCameras()
    return 1
    
#кнопка add_photos
def btn_click():
    # создание проекта
    doc = Metashape.app.document
    crs = Metashape.app.getCoordinateSystem("Select Coordinate System", doc.chunk.crs)
    doc.chunk.crs = crs
    path = Metashape.app.getSaveFileName("Save Project As")
    try:
        doc.save(path)
    except RuntimeError:
        Metashape.app.messageBox("Can't save project")
    name_dir_photo = ui.textEdit.toPlainText()

    # добавление снимков
    files_list = []
    for root, dirs, files in os.walk(name_dir_photo):
        for filename in files:
            files_list.append(filename)
    myLogText = "Добавлено: "+str(len(files_list))+" фото"
    showInfoMsg(myLogText)
    os.chdir(name_dir_photo)
    global mychunk
    mychunk = Metashape.app.document.addChunk()
    mychunk.addPhotos(files_list)
    camera = mychunk.cameras[0]
    camera.photo.meta["Exif/FocalLength"]

#выбор папки
def getDirectory():
    dirlist = QtWidgets.QFileDialog.getExistingDirectory()
    ui.textEdit.setPlainText(format(dirlist))

# создание окошка для инфо-сообщений
info_msg = QMessageBox()
info_msg.setIcon(QMessageBox.Information)
info_msg.setInformativeText('')
info_msg.setWindowTitle('  ')

def showInfoMsg(mstring):
    info_msg.setInformativeText(mstring)
    info_msg.exec_()



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


ui.pushButton.clicked.connect(getDirectory)
ui.pushButton_3.clicked.connect(btn_click)
ui.pushButton_2.clicked.connect(btn_split)
