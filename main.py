from sys import argv
from functools import reduce
from itertools import count, cycle

"""Задача 1"""

from sys import argv


script_name, work_time, wage, bounty = argv

salary = int(work_time) * int(wage) + int(bounty)
print(salary)


"""Задача 2"""


def list_sort(my_list):
    for i in range(1, len(my_list)):
        if my_list[i] > my_list[i-1]:
            x = max(my_list[i], my_list[i-1])
            yield x


list_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
gen = list_sort(list_1)
print([el for el in gen])


"""Задача 3"""


print([i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])


"""Задача 4"""


def search(my_list):
    for i in my_list:
        if my_list.count(i) == 1:
            yield i


list_1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
gen = search(list_1)
print([el for el in gen])


"""Задача 5"""


my_list = [i for i in range(100, 1001, 2)]
print(reduce(lambda x, y: x * y, my_list))


"""Задача 6, первый итератор"""


script_name, limit_1, limit_2 = argv

numbers = []
for el in count(int(limit_1)):
    if el > int(limit_2):
        break
    else:
        numbers.append(el)

print(numbers)


"""Задача 6, второй итератор"""


script_name, x = argv

my_list_1 = [i**2 for i in range(int(x)) ]
my_list_2 = []
for el in cycle(my_list_1):
    if len(my_list_2) < 32:
        my_list_2.append(el)
    else:
        break

print(my_list_2)


"""Задача 7"""


def fact(n):
    result = 1
    for i in count(1):
        if i <= n:
            result *= i
            yield result
        else:
            break


fact_list = []
for el in fact(10):
    fact_list.append(el)
print(fact_list)