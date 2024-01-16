import math


def get_sage_sqrt(num):
    try:
        if str(type(num)) == "<class 'str'>":
            raise TypeError(f'Корень берется от числа, не строки {num}')
        elif num < 0:
            raise ValueError(f'Не могу взять корень от отрицательного числа {num}')
        else:
            sqrt_num = math.sqrt(num)
            return sqrt_num
    except (ValueError, TypeError) as exc:
        return exc


# Тестовые случаи
numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}")
