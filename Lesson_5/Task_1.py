# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os


def str_to_tuple(path):
    file_dir, file_name = os.path.split(path)
    file_name, file_format = os.path.splitext(file_name)
    return file_dir, file_name, file_format


def main():
    path = 'D:\Python\Seminar\Task_1.py'
    file_path, file_name, file_format = str_to_tuple(path)
    print(f"Путь: {file_path} \nНазвание: {file_name} \nФормат: {file_format}")


if __name__ == '__main__':
    main()
