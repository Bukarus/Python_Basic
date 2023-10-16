def intersect_without_sets(array1, array2, array3):
    array_intersection_without_sets = [y for y in (x for x in array1 if x in array2) if y in array3]
    return array_intersection_without_sets


def intersect_with_sets(array1, array2, array3):
    set_intersection_with_sets = set(array1) & set(array2) & set(array3)
    return set_intersection_with_sets


def difference_without_sets(array1, array2, array3):
    array_without_2_3 = [x for x in array1 if x not in (array2 + array3)]
    return array_without_2_3


def difference_with_sets(array1, array2, array3):
    set_without_2_3_with_sets = set(array1) - set(array2) - set(array3)
    return set_without_2_3_with_sets


array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]


print(intersect_without_sets(array_1, array_2, array_3))
print(intersect_with_sets(array_1, array_2, array_3))
print(difference_without_sets(array_1, array_2, array_3))
print(difference_with_sets(array_1, array_2, array_3))
