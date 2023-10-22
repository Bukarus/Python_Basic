def my_zip(iter_1, iter_2):
    if isinstance(iter_1, dict):
        iter_1 = list(iter_1.values())
    if isinstance(iter_2, dict):
        iter_2 = list(iter_2.values())
    length = min(len(iter_1), len(iter_2))
    return ((iter_1[i], iter_2[i]) for i in range(length))


string = 'abcd'
my_tuple = (10, 20, 30, 40)
my_dict = {1: 'm', 2: 'n'}
print(my_zip(string, my_tuple))
for element in my_zip(string, my_tuple):
    print(element)
