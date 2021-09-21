"""
Написать рекурсивную функцию fibonacci, которая будет возвращать n-ый элемент
"""


def fibonacci(n, first=0, second=1, current=0):
    if current < n:
        return fibonacci(n, first=second, second=first + second, current=current + 1)
    else:
        return first


print(fibonacci(1))
