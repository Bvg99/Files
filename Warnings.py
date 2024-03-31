import warnings

volume = None
mass = None
def density(volume, mass):
    try:
        if mass < 0.01:
            warnings.warn('значение близко к нулю', UserWarning)
    except UserWarning as e:
        print(f'Предупреждение перехвачено: {e}')
    density = volume / mass
    print('density: ', density)

warnings.simplefilter('error') # Превращает предупреждение в исключение, программа дальше не работает
#warnings.simplefilter('ignore') # Блокирует печать предупреждения
#warnings.simplefilter('always') # Всегда печатает соответствующее предупреждение

density(5, 0.0001)
print('Calculation is OK')
