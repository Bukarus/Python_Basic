violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

quantity = int(input('Сколько песен выбрать? '))
time = sum([violator_songs[input('Название {} песни: '.format(number + 1))] for number in range(quantity)])

print('Общее время звучания песен: {} минуты'.format(time))
