import os
import logging
from collections import namedtuple

# Настройка логирования
logging.basicConfig(filename='file_info.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Определение объекта namedtuple для хранения информации о файлах и каталогах
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

def collect_file_info(directory_path):
    try:
        # Проверка существования директории
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The specified directory '{directory_path}' does not exist.")

        # Получение списка файлов и каталогов в указанной директории
        items = os.listdir(directory_path)

        # Итерация по каждому элементу в директории
        for item in items:
            item_path = os.path.join(directory_path, item)
            is_directory = os.path.isdir(item_path)

            # Получение имени файла/каталога без расширения
            name, extension = os.path.splitext(item) if not is_directory else (item, None)

            # Получение названия родительского каталога
            parent_directory = os.path.basename(directory_path)

            # Создание объекта FileInfo и запись в лог
            file_info = FileInfo(name, extension, is_directory, parent_directory)
            logging.info(file_info)

            # Рекурсивный вызов для подкаталогов
            if is_directory:
                collect_file_info(item_path)

    except Exception as e:
        # Обработка исключений и запись в лог
        logging.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    import sys

    # Проверка, что передан аргумент с путем к директории
    if len(sys.argv) != 2:
        print("Usage: python main.py /path/to/directory")
    else:
        directory_path = sys.argv[1]
        collect_file_info(directory_path)
