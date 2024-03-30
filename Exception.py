s = 's'
def string_to_int(s): # добавить обработку ValueError
    try:
        return int(s)
    except ValueError:
        return (f'ошибка:невозможно преобразовать {s} в целое число')
    finally:
        print('Работаем!')



filename = 'two.txt'
def read_file(filename): # добавить обработку FileNotFoundError, IOError
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f'Ошибка: файл {filename} не найден'
    except IOError:
        return f'Ошибка ввоода/вывода при работе с файлом {filename}'


a = 1
b = 0
def divide_numbers(a, b): # добавить обработку ZeroDivisionError, TypeError
    try:
        return a / b
    except ZeroDivisionError:
        return 'Ошибка: деление на ноль'
    except TypeError:
        return 'Ошибка: аргументы должны быть числами'



lst = [a, b]
def access_list_element(lst, index): # добавить обработку IndexError, TypeError
    try:
        return lst[index]
    except IndexError:
        return f'Ошибка: индекс {index} вне диапазона списка'

print(string_to_int(s))

print(read_file(filename))

print(divide_numbers(a, b))

print(access_list_element(lst, 2))