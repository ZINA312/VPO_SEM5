import unittest
from io import StringIO
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Task1 import *

# Класс с юнит-тестами
class TestPrintMessages(unittest.TestCase):
    def test_output(self):
        for _ in range(100):  # Проверяем 100 раз
            # Перенаправляем stdout для захвата выводимых данных
            captured_output = StringIO()
            sys.stdout = captured_output

            # Вызываем тестируемую функцию
            print_messages()

            # Восстанавливаем stdout
            sys.stdout = sys.__stdout__

            # Получаем вывод
            output = captured_output.getvalue().splitlines()

            # Проверяем, что первая и вторая строки соответствуют ожиданиям
            self.assertEqual(output[0], "Hello,world!")
            self.assertEqual(output[1], "Andhiagain!")
            
            # Проверяем третью строку
            exclamations = output[2]
            count = exclamations.count('!')

            # Проверяем, что строка состоит только из восклицательных знаков
            self.assertTrue(all(char == '!' for char in exclamations))
            # Проверяем, что количество восклицательных знаков в диапазоне от 5 до 50
            self.assertTrue(5 <= count <= 50)

# Запуск тестов
if __name__ == '__main__':
    unittest.main()