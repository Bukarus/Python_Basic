def key_value(some_dict, search_key, depth=-1):
    result = None
    if depth == 0:
        result = None
    elif search_key in some_dict:
        result = some_dict[search_key]
    else:
        for key, value in some_dict.items():
            if isinstance(value, dict):
                result = key_value(value, search_key, depth - 1)
                if result:
                    break
    return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


find_key = input('Введите ключ: ')
enter_max = input('Хотите ввести максимальную глубину? Y/N: ').lower()

if enter_max == 'y':
    max_depth = int(input('Введите максимальную глубину: '))
    print('Значение ключа: ', key_value(site, find_key, depth=max_depth))
elif enter_max == 'n':
    print('Значение ключа: ', key_value(site, find_key))
