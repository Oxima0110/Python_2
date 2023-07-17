# Напишите программу, которая получает целое число и 
# возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.


BASE = 16

def get_number(input_string:str)->int:
    '''
    Получение числа
    '''
    while True:
        try:
            num = int(input(input_string))
            if num > 0: 
                return num
            else:
                print('Число должно быть положительным')
        except ValueError:
            print('Это не то ...')

def get_res(num: int) -> str:
    '''
    перевод в шестнадцатеричное строковое представление
    '''
    res = ''
    while num != 0:
        num, digit = divmod(num, BASE)
        if  digit < 10:
            res = str(digit) + res
        else:
            match digit:
                case 10:
                    res = 'a' + res
                case 11:
                    res = 'b' + res
                case 12:
                    res = 'c' + res
                case 13:
                    res = 'd' + res
                case 14:
                    res = 'e' + res
                case 15:
                    res = 'f' + res
    return res
    

num = get_number('Введите число для преобразования:\n')
print(f'Число {num} в шестнадцатеричном представлении: {get_res(num)}, проверка:{hex(num)}')

    
    