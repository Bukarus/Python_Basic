def extend_lst(*args):
    lst = list()
    for item in args:
        if isinstance(item, int):
            lst.append(item)
        else:
            lst.extend(extend_lst(*item))
    return lst



nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

print(extend_lst(nice_list))
