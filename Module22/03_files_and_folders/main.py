import os

def calc_file(user_path):
    # print('переходим ', user_path)
    count_of_dir = 0
    count_of_files = 0
    lst_of_sizes = []
    for i_elem in os.listdir(user_path):
        path = os.path.join(user_path, i_elem)
        # print(' смотрим', path)
        if os.path.isfile(path):
            count_of_files += 1
            lst_of_sizes.append(os.path.getsize(path))
            # print(path)
        elif os.path.isdir(path):
            count_of_dir += 1
            result = calc_file(path)
            if result:
                lst_of_sizes.extend(result[0])
                count_of_dir += result[1]
                count_of_files += result[2]
    return lst_of_sizes, count_of_dir, count_of_files


user_dir = os.path.abspath(os.path.join(r"C:\Users\Ruslan\PycharmProjects\Python_Basic\Module17"))
# print('---', len(calc_file(user_dir)[0]))
result = calc_file(user_dir)
print(user_dir)
print('Размер каталога (в Кб): ', round(sum(result[0])/1024, 2))
print('Количество подкаталогов: ', result[1])
print('Количество файлов: ', result[2])
