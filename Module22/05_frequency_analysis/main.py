def count_symbols(file):
    user_dict = {}
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    for i_line in file:
        for char in i_line:
            char = char.lower()
            if char in alphabet:
                if char in user_dict:
                    user_dict[char] += 1
                else:
                    user_dict[char] = 1
    return user_dict


file_out = open('text.txt', 'r', encoding='utf-8')
file_in = open('analysis.txt', 'w', encoding='utf-8')

symbols_dict = count_symbols(file_out)
quantity_symbols = sum(symbols_dict.values())

sorted_list = []
for key, value in symbols_dict.items():
    frequency = round(value / quantity_symbols, 3)
    sorted_list.append((key, frequency))

sorted_list = sorted(sorted_list, key=lambda x: (-x[1], x[0]))

for val1, val2 in sorted_list:
    file_in.write('{} {} \n'.format(val1, val2))

file_out.close()
file_in.close()
