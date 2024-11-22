import os

# Функция для сохранения HTML-контента в файл
def save_html(filename, content):
    # Проверяем, существует ли файл
    if os.path.exists(filename):
        # Если существует, открываем его в режиме записи, чтобы удалить содержимое
        with open(filename, 'w') as file:
            file.write(content)  # Записываем новое содержимое
    else:
        # Если не существует, создаем файл и записываем содержимое
        with open(filename, 'w') as file:
            file.write(content)  

# Функция для генерации HTML-таблицы с заданным количеством строк
def generate_html_table(rows):
    # Проверка на корректность ввода (количество строк должно быть положительным)
    try:
        rows = int(rows)
    except:
        print("Неверный ввод")
        return "Неверный ввод"
    if rows <= 0:
        print("Неверный ввод")
        return "Неверный ввод"

    # Начало HTML-кода с добавлением стилей
    html = '<html><head><style>\n'
    html += 'table { border-collapse: collapse; width: 100%; }\n'
    html += 'td { height: 30px; text-align: center; }\n'
    html += '</style></head><body>\n'
    html += '<table>\n'

    # Генерация строк таблицы с градиентом
    for i in range(rows):
        shade = int(255 - (255 / rows) * i)  # Вычисление оттенка серого
        color = f'rgb({shade}, {shade}, {shade})'
        html += f'  <tr style="background-color: {color};"><td></td></tr>\n'

    # Закрытие тегов и сохранение HTML в файл
    html += '</table>\n</body></html>'
    save_html("gradient.html", html)
    return html

if __name__ == "__main__":
    generate_html_table(input("Введите количество рядов:"))