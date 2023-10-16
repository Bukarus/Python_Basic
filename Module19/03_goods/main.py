goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# new_dict = dict()

for name, code in goods.items():
    total_cost = 0
    total_quantity = 0
    for item in store[code]:
        total_cost += item['quantity'] * item['price']
        total_quantity += item['quantity']
    print('{} - {} штук, стоимость - {} руб.'.format(name, total_quantity, total_cost))

    # new_dict[name] = {'стоимость': sum, 'количество': total_quantity}
# print(new_dict)
