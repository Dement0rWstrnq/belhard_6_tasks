"""
Написать рекурсивную функцию factorial, которая будет возвращать n-ый элемент

5! = 1 * 2 * 3 * 4 * 5 = 125
"""


def factorial(n, result=1, current=1):
    if current <= n:
        print(result)
        return factorial(n, current=current + 1, result=result * current)
    else:
        return result


print(factorial(5))
