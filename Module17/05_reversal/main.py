
answer = input('Введите строку, чтобы присутствовало как минимум 2 h:')
last_i = 0
first_i = 0



for i in range(len(answer)):
    if answer[i] == 'h':
        first_i = i
        print(i)
        break

for i in range(len(answer)-1, 0, -1):
    if answer[i] == 'h':
        last_i = i
        print(i)
        break

print(answer[last_i - 1:first_i:-1])

