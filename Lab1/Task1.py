import random

# Функция, которую будем тестировать
def print_messages():
    exclamation_count = random.randint(5, 50)
    exclamations = '!' * exclamation_count
    print("Hello, world!")
    print("Andhiagain!")
    print(exclamations)

if __name__ == "__main__":
    print_messages()