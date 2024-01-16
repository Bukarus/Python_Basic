line_count = 0
sym_sum = 0

with open('people.txt', 'r', encoding='utf-8') as people_file, open('errors.log', 'w', encoding='utf-8') as error_file:
    for i_line in people_file:
        try:
            line_count += 1
            length = len(i_line)
            if i_line.endswith('\n'):
                length -= 1
            if length < 3:
                raise BaseException
        except BaseException as esc:
            print('Ошибка: Длина {} строки меньше 3 символов'.format(line_count))
            error_file.write('Ошибка: Длина {} строки меньше 3 символов \n'.format(line_count))
        finally:
            sym_sum += length
    print(f'Общее количество символов: {sym_sum}')
