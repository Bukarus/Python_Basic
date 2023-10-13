def count_uppercase_lowercase(_text):
    # uppercase_count = len([x for x in text if x.isupper()])
    # lowercase_count = len([y for y in text if y.islower()])
    uppercase_count, lowercase_count = 0, 0
    for x in _text:
        if x.isupper():
            uppercase_count += 1
        elif x.islower():
            lowercase_count += 1
        else:
            continue

    return uppercase_count, lowercase_count


# Пример использования:
text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)
