
def analyzer_of_text(user_text):
    list_of_vowel = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    result_list = [char for char in user_text if char in list_of_vowel]
    return result_list


my_text = input('Введите текст: ')
my_list = analyzer_of_text(my_text)
print('Список гласных букв:', my_list)
print('Длина списка:', len(my_list))
