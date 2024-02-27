# Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

from pathlib import Path


def rename_files(target_file_name, counter, file_extension, target_file_extension, name_range=None):

    file_list = [f for f in Path().iterdir() if f.suffix == file_extension]
    count = 1
    for file in file_list:
        original_name = file.stem
        if name_range is not None:
            start_ch, end_ch = name_range
            if end_ch > len(original_name):
                end_ch = len(original_name)
            original_name = original_name[start_ch:end_ch]
            target_file_name = target_file_name[:start_ch] + original_name + target_file_name[end_ch:]

        new_name = f'{target_file_name}_{count:0{counter}d}.{target_file_extension}'
        file.rename(file.with_name(new_name))
        count += 1
