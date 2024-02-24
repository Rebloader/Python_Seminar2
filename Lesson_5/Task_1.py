# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def str_to_tuple(path):
    *directory, full_name = path.split('\\')
    file_name, file_format = full_name.split('.')
    file_path = '\\'.join(directory)
    return file_path, file_name, file_format


def main():
    path = 'D:\Python\Seminar\Task_1.py'
    file_path, file_name, file_format = str_to_tuple(path)
    print(f"Путь: {file_path} \nНазвание: {file_name} \nФормат: {file_format}")


if __name__ == '__main__':
    main()
