import random

sum_of_numbers = 0
with open('open_file.txt', 'w', encoding='utf-8') as open_file:
    while True:
        try:
            print(sum_of_numbers)
            number = int(input('Введите число: '))
            if 13 == random.randint(1, 13):
                raise BaseException('1')
            open_file.write(str(number) + '\n')
            sum_of_numbers += number
            # print(sum_of_numbers)
            if sum_of_numbers >= 777:
                raise StopIteration('2')
        except StopIteration as exc:
            print('Вы успешно выполнили условие для выхода из порочного цикла!')
            break
        except ValueError as exc:
            print('Введено неправильное значение!', exc)
        except BaseException as exc:
            print('Возникла непрогнозируемая ситуация случайным образом!', exc)
            break
