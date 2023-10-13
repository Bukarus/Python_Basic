string = input('Введите строку: ').split()
new_string = []

for word in string:
    new_word = ''.join([word[0].upper(), word[1:]])
    new_string.append(new_word)

print(' '.join(new_string))

"""
Есть команда title, надо ли было делать через нее? Я понимаю, что так было бы проще!
"""
