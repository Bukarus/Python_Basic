def shift_symbol(text, shift):
    remake_string = [text[(number + shift) % len(text)] for number in range(len(text))]
    return remake_string


def is_palindrome(text):
    return text == text[::-1]


string = input('Введите строку: ')
for i in range(len(string)):
    new_string = ''.join(shift_symbol(string, i))
    if is_palindrome(new_string):
        print('Можно сделать палиндром', new_string)
        break
else:
    print('Нельзя сделать палиндром')
