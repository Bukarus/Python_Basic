students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def make_info(dict_of_students):
    list_of_interests = set()
    list_of_names = []
    for info in dict_of_students.values():
        list_of_interests.update(set(info['interests']))
        list_of_names.append(info['surname'])
    return list_of_interests, len(''.join(list_of_names))


pairs = [(key, value['age']) for key, value in students.items()]
print('Полный список пар: "ID студента — возраст" {}'.format(pairs))

interest_list, total_family_length = make_info(students)
print('Полный список интересов всех студентов: {}'.format(interest_list))
print('Общая длина всех фамилий студентов: {}'.format(total_family_length))
