def calc_frequency(text):
    frequency = {}
    for symbol in text:
        if symbol in frequency:
            frequency[symbol] += 1
        else:
            frequency[symbol] = 1
    return frequency

def calc_invert_frequency(any_frequency):
    invert_dict = {}
    for key, value in any_frequency.items():
        if value in invert_dict:
            invert_dict[value].append(key)
        else:
            invert_dict[value] = [key]
    return invert_dict

the_frequency = calc_invert_frequency(calc_frequency(input("Введите текст: ")))

for letter, freq in the_frequency.items():
    print(letter, ':', freq)

