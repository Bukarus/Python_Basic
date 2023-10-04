
# any_list = []
# for x in range(4):
#     any_list.append([])
#     for y in range(3):
#         any_list[x].append(0)

# i = 1
#
# for y in range(3):
#     for x in range(4):
#         any_list[x][y] = i
#         i += 1

any_list = [[x + i * 4 for i in range(3)] for x in range(1, 5)]

print(any_list)




