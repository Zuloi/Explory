#!/usr/bin/python3

import shutil, tempfile
import os
import unittest
import pathlib
from main import (backup, make_directories, move_files)

class Tests(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()
        source_directory = "temp/sortierung/hallo.txt"
        #os.makedirs(source_directory)
       

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)

         

    def test_make_directories(self):
        target_directories = ["temp/sortiert/txt", "/sortiert/docx"]
        make_directories(target_directories)
        self.assertTrue(os.path.exists("temp/sortiert/txt") and os.path.exists("temp/sortiert/docx"))
      
    def test_move_files(self):
        source_directory = "temp/sortierung/hallo.txt"
        target_directories = ["temp/sortiert/txt", "temp/sortiert/docx"]
        file_types = ["hallo.txt", "*.docx"]
        move_files(source_directory, target_directories, file_types)
        self.assertTrue(os.path.exists("temp/sortiert/txt/hallo.txt"))
        
    def test_backup(self):
        backup_directory = "temp/backup"
        source_directory = "temp/sortierung/hallo.txt"
        backup(source_directory, backup_directory)
        self.assertTrue(os.path.exists("temp/backup/hallo.txt"))

if __name__ == '__main__':
    unittest.main()

