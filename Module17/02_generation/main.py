
import random

N = int(input('Введите количество чисел: '))
list_of_numbers = [(1 if x % 2 == 0 else x % 5) for x in range(N)]
print(list_of_numbers)