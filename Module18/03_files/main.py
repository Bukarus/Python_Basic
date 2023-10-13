special_symbols = tuple('@№$%^&\*()')
print(special_symbols)
ends = ('.txt', '.docx')

file_name = input('Введите название файла: ')

if file_name.startswith(special_symbols):
    print('Ошибка: название начинается на один из специальных символов.')
elif not file_name.endswith(ends):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно.')


