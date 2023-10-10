flag = True

while True:
    password = input('Введите пароль: ')

    len_of_digit = len([char for char in password if char.isdigit()])
    len_of_upper = len([char for char in password if char.isupper()])
    len_password = len(password)

    if len_of_digit < 3 or len_password < 8 or len_of_upper < 1:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break

