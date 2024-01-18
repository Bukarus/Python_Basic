def validate_strline(string):
    str_array = str(string).split()
    if len(str_array) < 3:
        raise IndexError('Не присутствуют все три поля!')
    if not str_array[0].isalpha():
        raise NameError('Поле «Имя» содержит НЕ только буквы')
    if not ('@' in str_array[1] and '.' in str_array[1]):
        raise SyntaxError('Поле «Имейл» НЕ содержит @ и . (точку)')
    if not (10 <= int(str_array[2]) <= 100):
        raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99')
    return True


with open('registrations.txt', 'r', encoding='utf-8') as reg_file, \
        open('registrations_good.log', 'w', encoding='utf-8') as good_file, \
        open('registrations_bad.log', 'w', encoding='utf-8') as bad_file:

    for i_line in reg_file:
        if i_line.endswith('\n'):
            i_line = i_line[:-1]
        try:
            if validate_strline(i_line):
                good_file.write(f'{i_line}\n')
        except (IndexError, NameError, SyntaxError, ValueError) as exc:
            bad_file.write("{: <34} {: <34}\n".format(i_line, str(exc)))
