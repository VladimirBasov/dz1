#print('Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:')
#duration = int(input('Введите секунды  '))
def convert_time(duration: int) -> str:
    if duration // 60 // 60 // 24 != 0:
        d = duration // 60 // 60 // 24
        print(d, 'days', end=' ')
    if duration // 60 // 60 % 24 != 0:
        h = duration // 60 // 60 % 24
        print(h, 'hours', end=' ')
    if duration // 60 % 60 != 0:
        m = duration // 60 % 60
        print(m, 'minutes', end=' ')
    if duration % 60 != 0:
        s = duration % 60
        print(s, 'seconds')


duration = 400153
result = convert_time(duration)
print(result)
