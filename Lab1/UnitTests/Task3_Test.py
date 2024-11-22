import unittest
from io import StringIO
from unittest.mock import patch
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Task3 import calculate_area, main

# Класс для юнит-тестов
class TestRectangleArea(unittest.TestCase):

    # Тестирование функции вычисления площади
    def test_calculate_area(self):
        self.assertEqual(calculate_area(5, 10), 50)
        self.assertEqual(calculate_area(0, 10), 0)
        self.assertEqual(calculate_area(5, 0), 0)
        self.assertEqual(calculate_area(0, 0), 0)
        self.assertEqual(calculate_area(3, 5), 15)
        self.assertEqual(calculate_area(2.5, 3.5), 8.75)

    # Тестирование некорректного ввода
    def test_invalid_input(self):
        with patch('builtins.input', side_effect=['five', 'ten']):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                main()
                self.assertIn("Ошибка: Ввод должен содержать только числа.", fake_out.getvalue())

        with patch('builtins.input', side_effect=['5', '-10']):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                main()
                self.assertIn("Ошибка: Длина и ширина должны быть неотрицательными.", fake_out.getvalue())

    # Тестирование корректного ввода
    def test_correct_input(self):
        with patch('builtins.input', side_effect=['5', '90']):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                main()
                self.assertEqual(fake_out.getvalue().strip(), "Площадь прямоугольника: 50.0")

# Запуск тестов, если файл выполняется как основной
if __name__ == '__main__':
    unittest.main()