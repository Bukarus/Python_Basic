def turn_over(fname_out):
    lst = []
    f_out = open(fname_out, 'r', encoding='utf-8')
    for i_line in f_out:
        lst.append(i_line)
    f_out.close()
    return lst


file_out = open('zen.txt', 'r', encoding='utf-8')
file_name_out = 'zen.txt'
for elem in turn_over(file_name_out)[::-1]:
    print(elem, end='')
