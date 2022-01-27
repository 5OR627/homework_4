from sys import argv
from itertools import count, cycle

# script_name, work_time, wage, bounty = argv
#
# salary = int(work_time) * int(wage) + int(bounty)
# print(salary)

script_name, limit_1, limit_2 = argv

numbers = []
for el in count(int(limit_1)):
    if el > int(limit_2):
        break
    else:
        numbers.append(el)

print(numbers)

# script_name, x = argv
# my_list_1 = []
# my_list_2 = []
# my_list_1 = [i**2 for i in range(int(x)) ]
# for el in cycle(my_list_1):
#     if len(my_list_2) < 32:
#         my_list_2.append(el)
#     else:
#         break
#
# print(my_list_2)
