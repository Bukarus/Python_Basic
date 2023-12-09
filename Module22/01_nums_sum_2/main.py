def file_sum_of_lines(file):
    summa = 0
    for i_line in file:
        if i_line.strip():
            summa += int(i_line.strip())
    return str(summa)


file_of_numbers = open('numbers.txt', 'r', encoding='utf-8')
file_of_answers = open('answers.txt', 'w', encoding='utf-8')

total_sum = file_sum_of_lines(file_of_numbers)
file_of_answers.write(total_sum)

file_of_numbers.close()
file_of_answers.close()
