# Напишите программу, которая принимает две строки вида 
# “a/b” - дробь с числителем и знаменателем. Программа 
# должна возвращать сумму и произведение* дробей. Для 
# проверки своего кода используйте модуль fractions.

import math
import fractions


def get_num(num:str)->int:
    '''
    получение числителя и знаменателя
    '''
    num1 = int(num[:num.find('/')])
    num2 = int(num[num.find('/')+1:])
    return num1, num2

def nod(num1:int, num2:int)->int:
    '''
    сокращение дроби
    '''
    res = math.gcd(num1, num2)
    num1 = int(num1 / res)
    num2 = int(num2 / res)
    return num1, num2

def addition(num1:int, num2:int)->int:
    '''
    сложение дроби
    '''
    numerator1, denominator1 = get_num(num1)
    numerator2, denominator2 = get_num(num2)
    if denominator1 == denominator2:
        res1 = numerator1 + numerator2
        res2 = denominator1
    else:
        nok = math.lcm(denominator1, denominator2)
        res1 = numerator1 * int(nok/denominator1) + numerator2 * int(nok/denominator2)
        res2 = nok
    res1, res2 = nod(res1, res2)
    return res1, res2

def division(num1:int, num2:int)->int:
    '''
    деление дроби
    '''
    numerator1, denominator1 = get_num(num1)
    numerator2, denominator2 = get_num(num2)
    res1 = numerator1 * denominator2
    res2 = numerator2 * denominator1
    res1, res2 = nod(res1, res2)
    return res1, res2

number1 = ('3/15')
number2 = ('4/18')

a, b = get_num(number1)
a1, b1 = get_num(number2)
f1 = fractions.Fraction(a, b) + fractions.Fraction(a1, b1)
f2 = fractions.Fraction(a, b) / fractions.Fraction(a1, b1)

res_add1, res_add2 = addition(number1, number2)
res_div1, res_div2 = division(number1, number2)

print(f'Результат сложения = {fractions.Fraction(res_add1, res_add2)}, проверка:{f1}')
print(f'Результат деления = {fractions.Fraction(res_div1, res_div2)}, проверка:{f2}')
