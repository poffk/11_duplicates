from os import walk
from os.path import getsize, join
from collections import Counter
import argparse


def parse_path():
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_dir',
                        help='enter the filepath to your directory')
    return parser.parse_args()


def get_name_size_of_all_files(path_to_folder):
    list_of_files = []
    for dir_path, dir_names, file_names in walk(path_to_folder):
        for file_name in file_names:
            list_of_files.append({
                'info_about_file': (file_name, getsize(join(dir_path, file_name))),
                'filepath': join(dir_path, file_name)
            })
    return list_of_files


if __name__ == '__main__':
    parser = parse_path()
    path_start = parser.path_to_dir
    list_of_files = get_name_size_of_all_files(path_start)
    list_of_files.sort(key=lambda file: file['info_about_file'][0])
    files_attributes = [(file['info_about_file'][0], file['info_about_file'][1]) for file in list_of_files]
    counter_files = Counter(files_attributes)
    for file in list_of_files:
        if counter_files[file['info_about_file']] > 1:
            print('Файл {0} повторяется, путь: {1}' \
                  .format(file['info_about_file'][0], file['filepath']))