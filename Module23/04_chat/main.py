chat_messages = []
menu = {
    1: 'Посмотреть текущий текст чата.',
    2: 'Отправить сообщение (затем вводит сообщение).'
}
while True:
    try:
        user_name = input('Введите имя пользователя: ')
        for key, value in menu.items():
            print(f'{key}: {value}')
        number_of_item = int(input('Ваш выбор: '))
        if number_of_item == 1:
            for message in chat_messages:
                print(f'{message[0]}: {message[1]}')
        elif number_of_item == 2:
            new_message = input('Введите сообщение: ')
            chat_messages.append([user_name, new_message])
        else:
            raise ValueError
    except ValueError:
        print('Необходимо вводить число 1 или 2')


