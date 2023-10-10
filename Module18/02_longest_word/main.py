string = input('Введите строку: ').split()
max_str = ''

for word in string:
    if len(word) > len(max_str):
        max_str = word

print('Самое длинное слово: {}'.format(max_str))
print('Длина слова: {}'.format(len(max_str)))
