from os import walk
from os.path import getsize, join
from collections import Counter


def get_name_size_of_all_files(path_to_folder):
    list_of_files = []
    for dir_path, dir_names, file_names in walk(path_to_folder):
        for file_name in file_names:
            list_of_files.append((file_name, getsize(join(dir_path, file_name))))
    return list_of_files


if __name__ == '__main__':
    path_start = input('Введите папку для поиска файлов-дубликатов: ')
    list_of_files = get_name_size_of_all_files(path_start)
    counter_files = Counter(list_of_files)
    for file in counter_files:
        if counter_files[file] > 1:
                print('Дубликаты файла {0} встречаются {1} раз(а)' .format(file[0], counter_files[file]))