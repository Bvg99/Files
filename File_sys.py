import os
import time

# обход каталога

print('обход каталога')
directory = os.walk('C:\\Users\\Broris\\PycharmProjects\\Files')
print(directory)
for root, dirs, files in directory:
    print(files)

# формирование полного пути к файлу

print('формирование полного пути к файлу')
full_path = os.path.join('PycharmProjects', 'Files', 'one.txt')
print(full_path)

# получение и отображение времени последнего изменения файла

print('получение и отображение времени последнего изменения файла')

# с начала эпохи

print(os.path.getmtime('one.txt'))

# в структуре даты и времени
print(time.gmtime(os.path.getmtime('one.txt')))

# размер файла

print('размер файла')
print(os.path.getsize('one.txt'))

# получение родительской директории файла

print('родительская директория файла one.txt')
print(os.path.dirname(full_path))