#!/usr/bin/python3


import os, shutil, glob 
import sys
import logging
import logging.handlers

from PyQt5 import QtWidgets                             #type: ignore   # pylint: disable=no-name-in-module
from PyQt5.QtWidgets import QApplication, QMainWindow   #type: ignore   # pylint: disable=no-name-in-module

from explory.errors.errors import (Window_Error, Backup_Error, Make_Directories_Error, Sort_Error, Unmove_Files_Error, Delete_Backup_Error, Delete_Sort_Error) #type: ignore # pylint: disable=no-name-in-module


class MyWindow(QMainWindow):
    source_directory = "./Data/Sortierung" #Path where your files are at the moment 
    backup_directory = "./Data/Backup" #Path where your files will be backuped
    base_target_directory = "./Data/sortiert/" #Basepath you want to move your files to
    target_directories = ["./Data/sortiert/txt", "./Data/sortiert/docx"] #Path you want to move your files to 
    file_types = ["*.txt", "*.docx"]
    

    def __init__(self):     
        super(MyWindow,self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("EXPLORY")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Sortierung")
        self.label.move(30,100)

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Start")
        self.button.move(100,100)
        self.button.clicked.connect(lambda: sort(self.source_directory, self.backup_directory, self.target_directories, self.file_types))
        
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Backup")
        self.label.move(30,150)

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Start")
        self.button.move(100,150)
        self.button.clicked.connect(lambda: backup(self.source_directory, self.backup_directory))

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Rückgängig")
        self.label.move(30,200)

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Start")
        self.button.move(100,200)
        self.button.clicked.connect(lambda: undo_sort(self.source_directory, self.backup_directory, self.base_target_directory))

def main():
    logfile()
    window()

def logfile():
    handler = logging.handlers.WatchedFileHandler(
    os.environ.get("LOGFILE", "./Data/LOGFILE/explory.log"))
    formatter = logging.Formatter(logging.BASIC_FORMAT)
    handler.setFormatter(formatter)
    root = logging.getLogger()
    root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
    root.addHandler(handler)

def window():
    try:    
        app = QApplication(sys.argv)
        win = MyWindow()
        win.show()
        sys.exit(app.exec_())
    except:
        logging.info("window was closed")
        raise Window_Error("window can't be built")

def sort(source_directory, backup_directory, target_directories, file_types):
    backup(source_directory, backup_directory)
    make_directories(target_directories)
    move_files(source_directory, target_directories, file_types)

def make_directories(target_directories):
    try:
        for target_directory in target_directories:
            if os.path.exists(target_directory):
                shutil.rmtree(target_directory)
            os.makedirs(target_directory)
    except:
        logging.error("making directories failed")
        raise Make_Directories_Error("making directories failed")

def move_files(source_directory, target_directories, file_types):
    try:
        for file_type, target_directory in zip(file_types, target_directories):
            files = glob.iglob(os.path.join(source_directory, file_type )) 
            for file in files: 
                if os.path.isfile(file): 
                    shutil.move(file, target_directory) 
    except:
        logging.error("sort failed")
        raise Sort_Error("sort failed")

def backup(source_directory, backup_directory):
    try:
        if os.path.exists(backup_directory):
            shutil.rmtree(backup_directory)
        shutil.copytree(source_directory, backup_directory)
    except:
        logging.error("backuping failed")
        raise Backup_Error("backuping failed")

def undo_sort(source_directory, backup_directory, base_target_directory):
    unmove_files(source_directory, backup_directory)
    delete_backup(backup_directory)
    delete_sort(base_target_directory)

def unmove_files(source_directory, backup_directory):
    try:
        if os.path.exists(source_directory):
            shutil.rmtree(source_directory)
        shutil.copytree(backup_directory, source_directory)
    except:
        logging.error("unmove files failed")
        raise Unmove_Files_Error("unmove files failed")

def delete_backup(backup_directory):
    try:
        if os.path.exists(backup_directory):
            shutil.rmtree(backup_directory)
    except:
        logging.error("deleting backup failed")
        raise Delete_Backup_Error("deleting backup failed")
    
def delete_sort(base_target_directory):
    try:
        if os.path.exists(base_target_directory):
            shutil.rmtree(base_target_directory)
    except:
        logging.error("deleting sort failed")
        raise Delete_Sort_Error("deleting sort failed")

if __name__ == "__main__":
    main()
