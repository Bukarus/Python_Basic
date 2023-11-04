def sum(*args):
    summa = 0
    for item in args:
        if isinstance(item, int):
            summa += item
        else:
            summa += sum(*item)
    return summa


print(sum(1, 2, 3))
print(sum([[1, 2, [3]], [1], 3]))
