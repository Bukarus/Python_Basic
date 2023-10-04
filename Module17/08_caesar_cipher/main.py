# TODO здесь писать код
def char_shift(symbol, shift):
    alphabet = [chr(i) for i in range(ord('а'), ord('я') + 1)]
    for i in range(len(alphabet)):
        if symbol == alphabet[i]:
            symbol = alphabet[(i + shift) % len(alphabet)]
            break
    return symbol

message = input('Введите сообщение: ')
shift = int(input('Сдвиг: '))


new_message = (''.join([char_shift(symbol, shift) for symbol in message]))
print(new_message)


