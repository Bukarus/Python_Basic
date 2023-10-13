string_1 = input('Введите первую строку: ')
string_2 = input('Введите вторую строку: ')

shift = string_1.find(string_2[0])
string_shifted = ''.join([string_2[(i + len(string_2) - shift) % len(string_2)] for i in range(len(string_2))])

if string_1 == string_shifted:
    print("Первая строка получается из второй со сдвигом {}".format(shift))
else:
    print("Первую строку нельзя получить из второй с помощью циклического сдвига.")




