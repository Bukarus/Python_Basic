ip_address = input('Введите IP-адрес: ').split('.')

if len(ip_address) != 4:
    print('Адрес — это четыре числа, разделённые точками.')
else:
    for item in ip_address:
        if not item.isdigit():
            print('{} - это не целое число.'.format(item))
            break
        elif int(item) > 255:
            print('{} превышает 255.'.format(item))
            break
    else:
        print('IP-адрес корректен.')
