import random

list_numbers = [random.randint(0, 100) for _ in range(10)]
print(f'Оригинальный список: {list_numbers}')

# Первый способ
new_list = [(list_numbers[i], list_numbers[i + 1]) for i in range(0, len(list_numbers), 2)]
print(f'Новый список: {new_list}')

# Второй способ
new_list2 = []
counter = 0
pair = []

for element in list_numbers:
    pair.append(element)
    counter += 1
    if counter == 2:
        new_list2.append(tuple(pair))
        pair.clear()
        counter = 0

print('Новый список другим способом: {}'.format(new_list2))


# Третий способ
list_one = list_numbers[0::2]
list_two = list_numbers[1::2]
# print(list_one)
# print(list_two)
print('Новый список третим способом: {}'.format(list(zip(list_one, list_two))))
