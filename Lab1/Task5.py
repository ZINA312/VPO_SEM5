import os

def find_files_with_extension(directory, extension):
    # Проверяем, существует ли директория
    if not os.path.exists(directory):
        print(f"Директория {directory} не существует.")
        return []

    # Проверяем, начинается ли расширение с точки
    if not extension.startswith('.'):
        print("Расширение должно начинаться с точки.")
        return []

    found_files = []
    # Проходим по всем файлам в директории и поддиректориях
    for root, _, files in os.walk(directory):
        for file in files:
            # Если файл имеет нужное расширение, добавляем его в список
            if file.endswith(extension):
                found_files.append(os.path.join(root, file))
    return found_files

if __name__ == "__main__":
    files = find_files_with_extension(input("Введите директорию:"), input("Введите расширение:"))
    print(', '.join(files))