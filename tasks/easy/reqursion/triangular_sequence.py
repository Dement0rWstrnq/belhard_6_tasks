"""
Написать функцию triangular_sequence, которая принимает n и возвращает
последовательность следующего вида:

1
22
333
4444
55555
...

Например:

n = 3:
1
22
333

n = 6:
1
22
333
4444
55555
666666
"""


def triangular_sequence(n, some_str='', current=1):
    if n >= current:
        some_str += f'{str(current) * current}\n'
        return triangular_sequence(n, some_str, current=current + 1)
    else:
        return some_str


print(triangular_sequence(6))
