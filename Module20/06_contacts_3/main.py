telephone_book = {}

while True:

    print('Введите номер действия')
    print('1. Добавить контакт')
    print('2. Найти человека')
    answer = int(input(' '))

    if answer == 1:
        family_name = input('Введите имя и фамилию нового человека (через пробел): ').split()
        family_name = tuple(family_name)
        if telephone_book.get(family_name, None):
            print('Такой человек уже есть в контактах.')
        else:
            telephone_number = int(input('Введите номер телефона: '))
            telephone_book[family_name] = telephone_number
        print('Текущий словарь контактов: {}'.format(telephone_book))
    elif answer == 2:
        search_family = input('Введите фамилию человека: ')
        for (family, name), number in telephone_book.items():
            if search_family == family:
                # string_family, string_name = key
                print(family, name, number)
    else:
        print('Можно вводить 1 или 2')
