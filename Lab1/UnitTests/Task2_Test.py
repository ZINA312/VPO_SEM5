from unittest.mock import patch
from io import StringIO
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Task2 import *

# Юнит-тесты для функций ввода и вывода
class TestPeopleInput(unittest.TestCase):

    # Тестовый случай для корректного ввода
    def test_valid_input(self):
        inputs = iter(["John", "Doe", "30", "Jane", "Smith", "25", "exit"])
        expected_output = "Doe John 30\nSmith Jane 25\nМинимальный возраст: 25\nМаксимальный возраст: 30\nСредний возраст: 27.50\n"
        z
        with patch('builtins.input', lambda _: next(inputs)), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            people = input_people()  # Вызываем функцию ввода
            print_people(people)      # Вызываем функцию вывода
            self.assertEqual(mock_stdout.getvalue(), expected_output)  # Проверяем вывод

    # Тестовый случай для неверного ввода возраста
    def test_invalid_age_input(self):
        inputs = iter(["John", "Doe", "not_a_number", "exit"])
        expected_output = "Ошибка: Введите корректный возраст.\n"
        
        with patch('builtins.input', lambda _: next(inputs)), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            people = input_people()  # Вызываем функцию ввода
            print_people(people)      # Вызываем функцию вывода
            self.assertEqual(mock_stdout.getvalue(), expected_output)  # Проверяем вывод

    # Тестовый случай для команды выхода
    def test_exit_command(self):
        inputs = iter(["exit"])
        expected_output = ""
        
        with patch('builtins.input', lambda _: next(inputs)), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            people = input_people()  # Вызываем функцию ввода
            print_people(people)      # Вызываем функцию вывода
            self.assertEqual(mock_stdout.getvalue(), expected_output)  # Проверяем вывод

    # Тестовый случай для неверного ввода имени
    def test_invalid_first_name(self):
        inputs = iter(["123", "Doe", "30", "exit"])
        expected_output = "Ошибка: Имя должно содержать только буквы.\n"
        
        with patch('builtins.input', lambda _: next(inputs)), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            people = input_people()  # Вызываем функцию ввода
            print_people(people)      # Вызываем функцию вывода
            self.assertEqual(mock_stdout.getvalue(), expected_output)  # Проверяем вывод

    # Тестовый случай для неверного ввода фамилии
    def test_invalid_last_name(self):
        inputs = iter(["John", "123", "30", "exit"])
        expected_output = "Ошибка: Фамилия должна содержать только буквы.\n"
        
        with patch('builtins.input', lambda _: next(inputs)), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            people = input_people()  # Вызываем функцию ввода
            print_people(people)      # Вызываем функцию вывода
            self.assertEqual(mock_stdout.getvalue(), expected_output)  # Проверяем вывод

# Основной блок для запуска тестов
if __name__ == "__main__":
    unittest.main()