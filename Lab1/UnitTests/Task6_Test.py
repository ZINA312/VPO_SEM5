import os
import requests
import sys
import unittest
from unittest.mock import patch, mock_open
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Task6 import *

class TestDownloadFile(unittest.TestCase):

    @patch('requests.get')  # Замена requests.get на мок
    @patch('builtins.open', new_callable=mock_open)  # Замена open на мок
    def test_successful_download(self, mock_open, mock_get):
        mock_get.return_value.status_code = 200  # Успешный статус
        mock_get.return_value.content = b'Test content'  # Контент для теста
        
        download_file('https://iis.bsuir.by/static/media/logo.8b355a4f.svg', 'test_folder')

        # Проверка, что open() был вызван с правильным путём
        mock_open.assert_called_once_with('test_folder\\logo.8b355a4f.svg', 'wb')

        # Проверка, что файл был записан с правильным содержимым
        mock_open().write.assert_called_once_with(b'Test content')

    @patch('requests.get')  # Замена requests.get на мок
    def test_download_http_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.HTTPError("HTTP Error")  # Симуляция HTTP ошибки

        with self.assertLogs(level='ERROR') as log:  # Логирование ошибок
            download_file('https://iis.bsuir.by/static/media/logo.8b3dfssdfsdfsdfsdf55a4f.svg', 'test_folder')

        # Проверка, что лог содержит ожидаемое сообщение об ошибке
        self.assertIn("Ошибка при загрузке файла: HTTP Error", log.output[0])

    @patch('requests.get')  # Замена requests.get на мок
    def test_invalid_url(self, mock_get):
        with self.assertLogs(level='ERROR') as log:  # Логирование ошибок
            with self.assertRaises(ValueError):  # Проверка на выброс ValueError
                download_file('invalid_url', 'test_folder')

        # Проверка, что лог содержит ожидаемое сообщение об ошибке
        self.assertIn("Ошибка: Некорректный URL", log.output[0])

if __name__ == '__main__':
    unittest.main()  # Запуск тестов