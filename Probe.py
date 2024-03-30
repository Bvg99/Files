# def string_to_int(s): # добавить обработку ValueError
#    return int(s)
# def read_file(filename): # добавить обработку FileNotFoundError, IOError
# with open(filename, 'r') as file:
#    return file.read()
# def divide_numbers(a, b): # добавить обработку ZeroDivisionError, TypeError
#     return a / b
# def access_list_element(lst, index): # добавить обработку IndexError, TypeError
#    return lst[index]

try:
    x = 10 / 0
except ZeroDivisionError:
    x = 0
print("Деление на ноль! Установлено значение x равное 0.")
print(x)
