nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]


new_list = [level_1 for level_3 in nice_list for level_2 in level_3 for level_1 in level_2]
print(new_list)