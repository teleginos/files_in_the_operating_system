import os
import time

directory = os.path.dirname(__file__)

for dirpath, dirname, filename in os.walk(directory):
    for file in filename:
        file_path = os.path.join(dirpath, file)

        last_modified_time = os.path.getmtime(file_path)
        formated_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(last_modified_time))

        file_size = os.path.getsize(file_path)
        parent_directory = os.path.dirname(file_path)

        print(f"Файл: {file_path}")
        print(f"Последние изменения: {formated_time}")
        print(f"Размер файла: {file_size} байт")
        print(f"Родительская директория: {parent_directory}")
        print("-" * 40)
