"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(some_list: list):
    some_set = set()
    set_long = len(some_set)
    for i in some_list:
        some_set.add(i)
        if len(some_set) > set_long:
            set_long += 1
            yield "No"
        else:
            yield "Yes"


some = [1, 2, 3, 2, 5, 6, 1, 7]
a = yes_or_no(some)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
