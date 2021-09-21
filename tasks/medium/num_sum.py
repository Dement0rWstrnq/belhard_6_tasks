"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

Можно пользоваться только функциями, операторами и условиями.
"""


def sum_of_numbers(value: int):
    i = 0
    for j in str(value):
        i += int(j)
    return i


print(sum_of_numbers(2323))
