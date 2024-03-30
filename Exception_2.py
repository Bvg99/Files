import random
class incorrect_age(Exception):
    def __init__(self, age):
        print(f'Возраст {age} не соответствует нашим требованиям')

class incorrect_status(Exception):
    def __init__(self):
        print('Нам семейные не интересны')


def welcome():
    print('Hello!')
    age = int(input('How old are you?   '))
    if age < 18:
        raise incorrect_age(age)
        return
    status = (input('Are you married? yes/no '))
    if status == 'yes':
        raise incorrect_status()
    global random_number
    random_number = random.randint(100, 999)
    print(f'Ваш разовый пароль для входа: {random_number} ')

try:
    welcome()
except incorrect_age:
    print(f'Еще раз - возраст не соответствует нашим требованиям!')
except incorrect_status:
    print('Еще раз - нам семейные не интересны!')
except NameError:
    print('Значит, не дошли до генерации пароля')


password = input('Введите ваш разовый пароль для входа:   ')
try:
    if int(password) == random_number:
        print('Вперед, к приключениям!')
    else:
        print('Некорректный пароль')
except NameError:
    print('Значит, не дошли до генерации пароля')
