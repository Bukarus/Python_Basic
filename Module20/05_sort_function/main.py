def sort_tuple(any_tuple=(1, 2, 3)):
    for element in any_tuple:
        if not isinstance(element, int):
            return any_tuple
    else:
        my_list = list(any_tuple)
        my_list.sort()
        return tuple(my_list)


# my_tuple = (6, 3, -1, 8, 4.3, 10, -5)
# print(sort_tuple(my_tuple))
