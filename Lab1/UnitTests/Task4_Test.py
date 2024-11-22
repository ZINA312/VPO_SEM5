import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Task4 import *

# Класс для тестирования генерации HTML-таблицы
class TestHTMLTableGeneration(unittest.TestCase):
    # Тестирование функции генерации таблицы с положительным количеством строк
    def test_generate_html_table(self):
        rows = 5
        expected_output = (
            '<html><head><style>\n'
            'table { border-collapse: collapse; width: 100%; }\n'
            'td { height: 30px; text-align: center; }\n'
            '</style></head><body>\n'
            '<table>\n'
            '  <tr style="background-color: rgb(255, 255, 255);"><td></td></tr>\n'
            '  <tr style="background-color: rgb(204, 204, 204);"><td></td></tr>\n'
            '  <tr style="background-color: rgb(153, 153, 153);"><td></td></tr>\n'
            '  <tr style="background-color: rgb(102, 102, 102);"><td></td></tr>\n'
            '  <tr style="background-color: rgb(51, 51, 51);"><td></td></tr>\n'
            '</table>\n</body></html>'
        )
        actual_output = generate_html_table(rows)  # Генерация таблицы
        self.assertEqual(actual_output.strip(), expected_output.strip())  # Сравнение с ожидаемым результатом

    # Тестирование функции с нулевым количеством строк
    def test_zero_raws_table(self):
        rows = 0
        expected_output = "Неверный ввод"
        actual_output = generate_html_table(rows)  # Генерация таблицы
        self.assertEqual(actual_output.strip(), expected_output.strip())  # Сравнение с ожидаемым результатом
        
    # Тестирование функции с отрицательным количеством строк
    def test_negative_raws_table(self):
        rows = -5
        expected_output = "Неверный ввод"
        actual_output = generate_html_table(rows)  # Генерация таблицы
        self.assertEqual(actual_output.strip(), expected_output.strip())  # Сравнение с ожидаемым результатом

    # Тестирование функции с строковым вводом 
    def test_string_raws_table(self):
        rows = "fdsfsd"
        expected_output = "Неверный ввод"
        actual_output = generate_html_table(rows)  # Генерация таблицы
        self.assertEqual(actual_output.strip(), expected_output.strip())  # Сравнение с ожидаемым результатом

# Запуск тестов, если файл выполняется напрямую
if __name__ == "__main__":
    unittest.main()