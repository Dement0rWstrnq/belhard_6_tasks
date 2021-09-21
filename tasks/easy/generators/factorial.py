"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""


def factorial(value=1, value_2=1):
    while True:
        yield value
        value_2 += 1
        value *= value_2


a = factorial()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
