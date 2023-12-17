# Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.


import os
from string import ascii_lowercase, digits
from random import choices, randint
from os import path

__all__ = ['create_files', 'extensions', 'is_dir_exists',
           'create_list', 'rename_files']

LEN_MIN = 6
LEN_MAX = 10
BYTE_MIN = 256
BYTE_MAX = 1024
FILE_QTS = 5
PATH_DIR = './task1'
FILE_END_NAME = 'mmm'
DIGIT_COUNTER = 3


def create_list():
    for dir_path, dir_name, file_name in os.walk(os.path.join(os.getcwd())):
        return file_name


def rename_files(init_ext: str, end_ext: str, region: list[int],
                 digit_qty: int = DIGIT_COUNTER,
                 file_end: str = FILE_END_NAME) -> None:
    create_list()
    count = 1
    for name in create_list():
        if init_ext == name.split('.')[-1]:
            nums = '0' * (digit_qty - len(str(count))) + str(count)
            new_name = f'{name[region[0]:region[1]]}{file_end}_{nums}.{end_ext}'
            os.replace(name, new_name)
            count += 1


def create_files(extension: str, len_min: int = LEN_MIN, len_max: int = LEN_MAX, byte_min: int = BYTE_MIN,
                 byte_max: int = BYTE_MAX, quantity: int = FILE_QTS) -> None:
    for i in range(quantity):
        name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(len_min, len_max)))
        data = bytes(randint(0, 255) for _ in range(randint(byte_min, byte_max)))
        with open(rf'{name}.{extension}', 'wb') as f:
            f.write(data)


def extensions(**kwargs):
    for ext, qty in kwargs.items():
        create_files(extension=ext, quantity=qty)


def is_dir_exists(directory=PATH_DIR, **kwargs) -> None:
    if not path.exists(directory):
        os.mkdir(directory)
    os.chdir(directory)
    extensions(**kwargs)


if __name__ == '__main__':
    is_dir_exists(rf'{PATH_DIR}', gif=1, txt=2, jpeg=6)
    rename_files('jpeg', 'md', [4, 2], 4, 'URNAME')
