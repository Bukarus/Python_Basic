def key_value(some_dict, search_key, depth=None):
    if depth is None:
        if isinstance(some_dict, dict):
            # print(some_dict)
            if search_key in some_dict.keys():
                answer = some_dict[search_key]
                return answer
            else:
                for key, value in some_dict.items():
                    # print(key)
                    answer = key_value(value, search_key)
                    if answer:
                        return answer
    elif depth > 0:
        if isinstance(some_dict, dict):
            # print(some_dict)
            depth -= 1
            if search_key in some_dict.keys():
                answer = some_dict[search_key]
                return answer
            else:
                for key, value in some_dict.items():
                    # print(depth)
                    answer = key_value(value, search_key, depth)
                    if answer:
                        return answer
    else:
        return None


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
