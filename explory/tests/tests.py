#!/usr/bin/python3

import shutil, tempfile
import os
import unittest
import pathlib
from explory import (make_directories, move_files, backup)

class Tests(unittest.TestCase):
    def setUp(self):
        os.makedirs("temp/sortierung/hallo.txt")
        os.makedirs("temp/sortierung/hallo.docx")


    def test_make_directories(self):
        target_directories = ["temp/sortiert/txt", "temp/sortiert/docx"]
        make_directories(target_directories)
        self.assertTrue(os.path.exists("temp/sortiert/txt") and os.path.exists("temp/sortiert/docx"))
      
    def test_move_files(self):
        source_directory = "temp/sortierung"
        target_directories = ["temp/sortiert/txt", "temp/sortiert/docx"]
        file_types = ["*.txt", "*.docx"]
        move_files(source_directory, target_directories, file_types)
        self.assertTrue(os.path.exists("temp/sortiert/txt/hallo.txt") and os.path.exists("temp/sortiert/docx/hallo.docx"))
        
    def test_backup(self):
        backup_directory = "temp/backup"
        source_directory = "temp/sortierung"
        backup(source_directory, backup_directory)
        self.assertTrue(os.path.exists("temp/backup/hallo.txt"))

    def tearDown(self):
        shutil.rmtree("temp/")

if __name__ == '__main__':
    unittest.main()

