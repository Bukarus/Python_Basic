

# alphabet = [chr(i) for i in range(ord('а'), ord('я') + 1)]
#
#
# def char_shift(symbol, _shift):
#     for i in range(len(alphabet)):
#         if symbol == alphabet[i]:
#             symbol = alphabet[(i + _shift) % len(alphabet)]
#             break
#     return symbol


message = input('Введите сообщение: ')
shift = int(input('Сдвиг: '))


# new_message = (''.join([char_shift(symbol, shift) for symbol in message]))
alphabet = [chr(i) for i in range(ord('а'), ord('я') + 1)]
new_message = [alphabet[(alphabet.index(char) + shift) % len(alphabet)]
               if char in alphabet else char for char in message]
new_message = ''.join(new_message)
print(new_message)
