file_out = open('first_tour.txt', 'r', encoding='utf-8')
file_in = open('second_tour.txt', 'w', encoding='utf-8')
file_in.write('\n')
coef = file_out.readline().strip()
number_of_second = 0
for i_line in file_out:
    lst = i_line.split()
    # print(lst)
    if int(lst[2]) > int(coef):
        number_of_second += 1
        file_in.write(str(number_of_second) + ')' + ' '.join(lst) + '\n')
file_in.seek(0)
file_in.write(str(number_of_second))
file_out.close()
file_in.close()
