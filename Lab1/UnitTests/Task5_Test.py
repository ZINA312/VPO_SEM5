import os
import sys
import unittest
import tempfile
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Task5 import *

class TestFindFilesWithExtension(unittest.TestCase):

    def setUp(self):
        # Создаем временную директорию для тестов
        self.test_dir = tempfile.TemporaryDirectory()
        self.file1 = os.path.join(self.test_dir.name, "file1.txt")
        self.file2 = os.path.join(self.test_dir.name, "file2.md")
        self.subdir = os.path.join(self.test_dir.name, "subdir")
        os.makedirs(self.subdir)  # Создаем поддиректорию
        self.file3 = os.path.join(self.subdir, "file3.txt")
        
        # Создаем тестовые файлы
        with open(self.file1, 'w'), open(self.file2, 'w'), open(self.file3, 'w'):
            pass  # Ничего не делаем, просто создаем файлы

    def tearDown(self):
        # Удаляем временную директорию после тестов
        self.test_dir.cleanup()

    def test_find_txt_files(self):
        # Тестируем поиск файлов с расширением .txt
        result = find_files_with_extension(self.test_dir.name, '.txt1')
        self.assertIn(self.file1, result)  # Проверяем, что file1.txt найден
        self.assertIn(self.file3, result)  # Проверяем, что file3.txt найден
        self.assertNotIn(self.file2, result)  # file2.md не должен быть найден

    def test_find_md_files(self):
        # Тестируем поиск файлов с расширением .md
        result = find_files_with_extension(self.test_dir.name, '.md')
        self.assertIn(self.file2, result)  # Проверяем, что file2.md найден
        self.assertNotIn(self.file1, result)  # file1.txt не должен быть найден
        self.assertNotIn(self.file3, result)  # file3.txt не должен быть найден

    def test_invalid_directory(self):
        # Тестируем некорректную директорию
        result = find_files_with_extension("invalid_directory", '.txt')
        self.assertEqual(result, [])  # Должен вернуть пустой список

    def test_invalid_extension(self):
        # Тестируем некорректное расширение
        result = find_files_with_extension(self.test_dir.name, 'txt')
        self.assertEqual(result, [])  # Должен вернуть пустой список
        result = find_files_with_extension(self.test_dir.name, '')
        self.assertEqual(result, [])  # Должен вернуть пустой список

if __name__ == '__main__':
    unittest.main()  # Запускаем тесты