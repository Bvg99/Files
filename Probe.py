# import requests
import warnings

# url = 'http://tomskrts.ru'
# data = requests.get(url)
# print(data.text)

def my_func():
    try:
        print('Перед генерацией предупреждения')
        warnings.warn('Это важное предупреждение', UserWarning)
        print('После генерации предупреждения')
    except UserWarning as e:
        print(f'Предупреждение было перехвачено как исключение: {e}')

# print('Пример 1: Фильтр Error')
# warnings.simplefilter('error', UserWarning)
# my_func()
# print('\n')

print('Пример 2: Фильтр Default')
warnings.simplefilter('default', UserWarning)
my_func()