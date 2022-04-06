def transform_string(number: int) -> str:
    if 10 < number < 20:
        return f'{number} процентов'
    elif number % 10 == 1:
        return f'{number} процент'
    elif 1 < number % 10 < 5:
        return f'{number} процента'
    else:
        return f'{number} процентов'



for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))