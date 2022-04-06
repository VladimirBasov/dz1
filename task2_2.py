def sum_list_1(dataset: list) -> int:
    numbers_list = []
    for i in range(1, 1000, 2):
        numbers_list.append(i ** 3 + 17)
    print(numbers_list)               # проверка списка
    all_summa = 0                     # сумма всех чисел делящихся на 7
    for i in numbers_list:
        summa = 0                     #сумма
        m = i
        while i > 0:
            summa += i % 10
            i //= 10
        if summa % 7 == 0:
            all_summa += m
    return all_summa
    print(all_summa)



my_list = []  # Соберите нужный список по заданию
result_1 = sum_list_1(my_list)
print(result_1)