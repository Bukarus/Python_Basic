def shift_symbol(text, shift):
    remake_string = [text[(number + shift) % len(text)] for number in range(len(text))]
    return remake_string


def is_palindrome(text):
    return text == text[::-1]


def can_make_palindrome(text):
    dict_sym = {}
    for char in text:
        if char in dict_sym:
            dict_sym[char] += 1
            if dict_sym[char] % 2 == 0:
                dict_sym.pop(char)
        else:
            dict_sym[char] = 1
    if len(dict_sym) > 1:
        return False
    else:
        return True



string = input('Введите строку: ')
if can_make_palindrome(string):
    print('Можно сделать палиндром')
else:
    print('Нельзя сделать палиндром')
