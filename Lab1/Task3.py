# Функция для вычисления площади прямоугольника
def calculate_area(length, width):
    return length * width

# Главная функция программы
def main():
    try:
        # Запрос ввода длины и ширины у пользователя
        length = float(input("Введите длину: "))
        width = float(input("Введите ширину: "))
    except ValueError:
        # Обработка ошибки, если ввод не является числом
        print("Ошибка: Ввод должен содержать только числа.")
        return

    # Проверка на неотрицательность
    if length < 0 or width < 0:
        print("Ошибка: Длина и ширина должны быть неотрицательными.")
        return

    # Вычисление площади
    area = calculate_area(length, width)
    # Вывод результата
    print(f"Площадь прямоугольника: {area}")

if __name__ == "__main__":
    main()