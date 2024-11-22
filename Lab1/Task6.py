import os
import requests
import logging

# Настройка логирования в файл с указанием кодировки
logger = logging.getLogger()
handler = logging.FileHandler('download_log.txt', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.ERROR)

def download_file(url, save_folder):
    try:
        if not url.startswith("http"):
            raise ValueError("Некорректный URL")

        response = requests.get(url)
        response.raise_for_status()

        filename = os.path.join(save_folder, url.split("/")[-1])
        os.makedirs(save_folder, exist_ok=True)

        with open(filename, 'wb') as file:
            file.write(response.content)

        print(f"Файл успешно сохранён как: {filename}")

    except ValueError as ve:
        logger.error(f"Ошибка: {ve}")
        raise
    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка при загрузке файла: {e}")
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    download_file(input("Введите URL: "), input("Введите путь сохранения файла: "))