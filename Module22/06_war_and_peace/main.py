import zipfile


def count_symbols(file):
    user_dict = {}
    for i_line in file:
        for char in i_line:
            char = char.lower()
            if char in user_dict:
                user_dict[char] += 1
            else:
                user_dict[char] = 1
    return user_dict


zfile = zipfile.ZipFile('voyna-i-mir.zip', 'r')
file_name = 'voyna-i-mir.txt'
zfile.extract(file_name)
f_open = open(file_name, 'r', encoding='utf-8')
symbols_dict = count_symbols(f_open)
symbols_dict = {k: v for k, v in sorted(symbols_dict.items(), key=lambda item: -item[1])}
for k, v in symbols_dict.items():
    print('символ {} - количество {}'.format(k, v))
