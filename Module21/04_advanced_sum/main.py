def sum(*args):
    lst = list()
    summa = 0
    for item in args:
        if isinstance(item, int):
            lst.append(item)
            summa += item
        else:
            lst.extend(sum(*item)[0])
            summa += sum(*item)[1]
    return lst, summa



print(sum(1, 2, 3))
print(sum([[1, 2, [3]], [1], 3]))
