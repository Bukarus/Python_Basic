import copy
import pprint


# def replace_string(dct, search_str, replace_str):
#     for key in dct:
#         if isinstance(dct[key], dict):
#             replace_string(dct[key], search_str, replace_str)
#         elif isinstance(dct[key], list):
#             for i in range(len(dct[key])):
#                 if isinstance(dct[key][i], dict):
#                     replace_string(dct[key][i], search_str, replace_str)
#                 elif isinstance(dct[key][i], str):
#                     dct[key][i] = dct[key][i].replace(search_str, replace_str)
#         elif isinstance(dct[key], str):
#             dct[key] = dct[key].replace(search_str, replace_str)
#     return dct


def replace_key(any_site, search_key, search_value, replace_value):
    if search_key in any_site:
        any_site[search_key] = any_site[search_key].replace(search_value, replace_value)
    for value in any_site.values():
        if isinstance(value, dict):
            replace_key(value, search_key, search_value, replace_value)


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


list_of_sites = list()
number_of_site = int(input('Введите количество сайтов: '))
for _ in range(number_of_site):
    new_site = copy.deepcopy(site)
    name = input('Введите название продукта для нового сайта: ')
    for srch_string in ('телефон', 'iphone'):
        replace_key(new_site, 'title', srch_string, name)
        replace_key(new_site, 'h2', srch_string, name)
    list_of_sites.append(new_site)
    for item in list_of_sites:
        pprint.pprint(item)
