# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней
# с учётом всех вложенных файлов и директорий.


import program
from pathlib import Path
from Save_files.csv_saver import save_as_csv
from Save_files.json_saver import save_as_json
from Save_files.pickle_saver import save_as_pickle


def main():
    str_path = input('Enter directory path: ')
    path = Path(str_path)
    results = program.bypass_directory(path)
    save_as_csv(results, 'directory_info.csv')
    save_as_json(results, 'directory_info.json')
    save_as_pickle(results, 'directory_info.pickle')


if __name__ == '__main__':
    main()
