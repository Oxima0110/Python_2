# Дан список повторяющихся элементов. Вернуть список с 
# дублирующимися элементами. В результирующем списке не 
# должно быть дубликатов.


my_list1 = [1, 2, 4, 2, 4, 6 , 8 , 9, 6, 4]
# Вариант1
res_list1 = []
for element in my_list1:
    if my_list1.count(element) != 1:
        res_list1.append(element)
        for i in range(my_list1.count(element)):
            my_list1.remove(element)
print(res_list1)

# Вариант2
my_list2 = [1, 2, 4, 2, 4, 6 , 8 , 9, 6, 4]
res_set = set()
for element in my_list2:
    if my_list2.count(element) != 1:
        res_set.add(element)
res_list2 = list(res_set)
print(res_list2)
