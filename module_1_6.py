my_dict = {'Nafis': 1967, 'Ainur': 1995, 'Aigul': 1995, 'Adelina': 2001}
print(my_dict)
print(my_dict['Nafis'])
my_dict['Ljaisan'] = 1972
my_dict.update({'Mother': 1945,
                'Dad': 1936})
my_dict.pop('Dad')
print(my_dict)

my_set = {24, 9, 1, 9, 2, 7, 2, 7, 27, 7, 9, 8, 28, 3, 'умер'}
print(my_set)
my_set.add(25)
my_set.add('неизвестно')
my_set.add('возможно')
my_set.discard(28)
print(my_set)
