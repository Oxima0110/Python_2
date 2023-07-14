# Напишите код, который запрашивает число и сообщает 
# является ли оно простым или составным. Используйте 
# правило для проверки: “Число является простым, если 
# делится нацело только на единицу и на себя”. Сделайте 
# ограничение на ввод отрицательных чисел и чисел 
# больше 100 тысяч.

def get_number(input_string:str)->int:
    '''
    Получение числа
    '''
    while True:
        try:
            num = int(input(input_string))
            if 0 < num < 100000: 
                return num
            else:
                print('Число должно быть положительным и меньше 100000')
        except ValueError:
            print('Это не то ...')

number = get_number('Введите число от 1 до 100000 \n')
flag = True
for i in range(2, number):
    if number % i == 0:
        flag = False
        break
if flag == True:
    result = 'Число '+ str(number) + ' является простым'
else:
    result = 'Число '+ str(number) + ' является составным'
print(result)