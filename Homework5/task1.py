# Напишите функцию, которая принимает на вход строку — 
# абсолютный путь до файла. Функция возвращает кортеж из трёх 
# элементов: путь, имя файла, расширение файла.


def tuple_road(data:str)->tuple:
    *road, name_file = data.split('\\')
    return ('\\'.join(road), 
            name_file.split('.')[0], 
            name_file.split('.')[1])

txt = "E:\Excel\Homework_2\Homework_2.xlsx"
print(tuple_road(txt))


