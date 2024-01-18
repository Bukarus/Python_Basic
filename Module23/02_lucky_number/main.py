import random

sum_of_numbers = 0
with open('open_file.txt', 'w', encoding='utf-8') as open_file:
    while sum_of_numbers < 777:
        try:
            print(sum_of_numbers)
            number = int(input('Введите число: '))
            if 13 == random.randint(1, 13):
                raise Exception('1')
            open_file.write(str(number) + '\n')
            sum_of_numbers += number
        except ValueError as exc:
            print('Введено неправильное значение!', exc)
        except Exception as exc:
            print('Возникла непрогнозируемая ситуация случайным образом!', exc)
            break
    else:
        print('Вы успешно выполнили условие по выходу из цикла!')
