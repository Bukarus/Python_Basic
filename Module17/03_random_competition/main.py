# TODO здесь писать код
import random

number_of_members = 20

list_1 = [round(random.uniform(0, 10), 2) for _ in range(number_of_members)]
list_2 = [round(random.uniform(0, 10), 2) for _ in range(number_of_members)]

print('Первая команда:', list_1)
print('Вторая команда:', list_2)

for i in range(number_of_members):
    if list_1[i] < list_2[i]:
        list_1[i] = list_2[i]

print('Победители тура:', list_1)
