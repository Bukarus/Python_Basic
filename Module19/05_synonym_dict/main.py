quantity_of_pairs = int(input('Введите количество пар: '))
dict_of_pairs = {}
for number in range(quantity_of_pairs):
    print('{}-я пара: '.format(number + 1), end=' ')
    answer = ("".join(input().split())).split('-') # убрал пробелы, разбил по дефизу
    dict_of_pairs[answer[0]] = answer[1]

while True:
    word = input('Введите слово: ')
    for key, value in dict_of_pairs.items():
        if word == key:
            print(value)
            break
        elif word == value:
            print(key)
            break
        else:
            continue
    if word == 'end':
        break