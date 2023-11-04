def split_list(lst):
    if isinstance(lst, list):
        sup_element = lst[-1]
        list_1 = [x for x in lst if x < sup_element]
        list_2 = [x for x in lst if x == sup_element]
        list_3 = [x for x in lst if x > sup_element]
        return list_1, list_2, list_3



def sort_list(lst):
    lst1, lst2, lst3 = split_list(lst)
    if len(lst1) > 1:
        lst1 = sort_list(lst1)
    if len(lst3) > 1:
        lst3 = sort_list(lst3)
    return lst1 + lst2 + lst3


print(sort_list([4, 9, 2, 7, 5, 1]))
