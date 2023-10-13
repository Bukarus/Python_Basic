string = input('Введите строку: ')

char_previous = ''
count_same = 1
new_string = ''

for char in string:

    if char_previous == '':
        count_same = 1
    elif char == char_previous:
        count_same += 1
    else:
        new_string = ''.join([new_string, char_previous, str(count_same)])
        count_same = 1
    char_previous = char

new_string = ''.join([new_string, char_previous, str(count_same)])
print('Закодированная строка:', new_string)
