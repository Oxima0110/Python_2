item_dict = {'Вася':{'рюкзак', 'палатка', 'котелок', 'фонарик'}, 
             'Коля':{'рюкзак', 'палатка', 'фонарик', 'спички'}, 
             'Миша':{'рюкзак', 'палатка', 'спички', 'велосипед'}}

name_list = []
for key in  item_dict.keys():
    name_list.append(key)

all_list = item_dict[name_list[0]]
for i in range(1, len(name_list)):
    all_list = all_list & item_dict[name_list[i]]
print(f'Вещи которые взялкаждый из друзей: {all_list}')

unic_list = set()
for i in range(len(name_list)):
    temp_set = set()
    for num, value in enumerate(item_dict.values(), start=0):
        if num != i:
            temp_set = temp_set.union(value)
    temp_set = item_dict[name_list[i]] - temp_set
    unic_list = unic_list.union(temp_set)
print(f'Список уникальных вещей: {unic_list}')

for i in range(len(name_list)):
    if i != len(name_list) - 1:
        all_list = item_dict[name_list[i+1]]
    else:
        all_list = item_dict[name_list[0]]
    for num, value in enumerate(item_dict.values(), start=0):
        if num != i:
            all_list = all_list & value
    all_list = all_list - item_dict[name_list[i]]
    if len(all_list) != 0:
        print(f'{name_list[i]} не взял {all_list}')

