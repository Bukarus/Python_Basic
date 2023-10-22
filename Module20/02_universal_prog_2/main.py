def is_prime(number):
    if number == 0:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    else:
        return True


def filter_of_prime_indexes(iter_obj):
    return [value for index, value in enumerate(iter_obj) if is_prime(index)]


# obj = 'О Дивный Новый мир!'
# print(filter_of_prime_indexes(obj))
