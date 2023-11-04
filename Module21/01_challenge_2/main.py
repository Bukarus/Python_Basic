def print_seq(num):
    if num == 1:
        value = 1
    else:
        value = print_seq(num - 1) + 1
    print(value)
    return value



answer = int(input('Введите число: '))
print_seq(answer)
