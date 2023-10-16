quantity_orders = int(input('Введите количество заказов: '))
dict_orders = {}
for order_number in range(quantity_orders):
    string = '{}-й заказ: '.format(order_number + 1)
    order = input(string).split()
    # order[2] = int(order[2])
    if order[0] in dict_orders:
        if order[1] in dict_orders[order[0]]:
            dict_orders[order[0]][order[1]] += int(order[2])
        else:
            dict_orders[order[0]][order[1]] = int(order[2])
    else:
        dict_orders[order[0]] = {}
        dict_orders[order[0]][order[1]] = int(order[2])

print(dict_orders)
