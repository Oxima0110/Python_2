# Напишите функцию принимающую на вход только ключевые 
# параметры и возвращающую словарь, где ключ — значение 
# переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое 
# представление.

def create_dict(**qwargs):
    res_dict = {}
    for item, qwarg in qwargs.items():
        if isinstance(qwarg, (list, dict, set, bytearray)):
            qwarg = str(qwarg)
        res_dict[qwarg] = item
    return res_dict

print(create_dict(a=[1, 2], b=2, c=(3, 8, 7)))
