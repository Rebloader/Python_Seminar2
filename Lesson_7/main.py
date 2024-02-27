import rename_files


def main():
    target_file_name = input('Введите желаемое имя файла: ')
    counter = int(input('Введите кодичество файлов: '))
    file_extension = input('Введите расширение файла для изменения: ')
    target_file_extension = input('Введите желаемое расширение файла: ')
    name_range = tuple(map(int, input('Введите диапазон: ').split(',')))

    rename_files.rename_files(target_file_name, counter, file_extension, target_file_extension, name_range)


if __name__ == '__main__':
    main()
