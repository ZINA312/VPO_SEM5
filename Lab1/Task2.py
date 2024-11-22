import unittest


# Определяем класс Person для представления людей
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name  # Сохраняем имя
        self.last_name = last_name      # Сохраняем фамилию
        self.age = age                  # Сохраняем возраст

    def __str__(self):
        # Возвращаем строковое представление человека
        return f"{self.last_name} {self.first_name} {self.age}"

# Функция для ввода данных о людях
def input_people():
    people = []  # Список для хранения объектов Person
    while True:
        try:
            # Запрашиваем имя
            first_name = input("Введите имя (или 'exit' для завершения): ")
            if first_name.lower() == 'exit':
                break  # Выход из цикла, если введено 'exit'
            if not first_name.isalpha():
                print("Ошибка: Имя должно содержать только буквы.")  # Проверка имени
                break
            
            # Запрашиваем фамилию
            last_name = input("Введите фамилию: ")
            if not last_name.isalpha():
                print("Ошибка: Фамилия должна содержать только буквы.")  # Проверка фамилии
                break
            
            # Запрашиваем возраст
            age = int(input("Введите возраст: "))  # Преобразуем ввод возраста в целое число
            people.append(Person(first_name, last_name, age))  # Создаем и добавляем объект Person
        except ValueError:
            print("Ошибка: Введите корректный возраст.")  # Обработка неверного ввода возраста
    return people  # Возвращаем список людей

# Функция для вывода данных о людях
def print_people(people):
    for person in people:
        print(person)  # Выводим каждого человека
    if people:  # Проверяем, что список не пуст
        ages = [person.age for person in people]  # Собираем возраста
        print(f"Минимальный возраст: {min(ages)}")  # Выводим минимальный возраст
        print(f"Максимальный возраст: {max(ages)}")  # Выводим максимальный возраст
        print(f"Средний возраст: {sum(ages) / len(ages):.2f}")  # Выводим средний возраст

if __name__ == "__main__":
    print_people(input_people())