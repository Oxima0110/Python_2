# Напишите программу банкомат. 
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не 
#    менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия 
#    начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на 
#    богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег


COMM_WITHDRAWAL = 1.5
COMM_REFIL = 3
TAX = 10
COMM_MIN = 30
COMM_MAX = 600
SUM_WORK = 50
MAX_ACCAUNT = 5000000
account = 0
count_refil = 0
count_withdrawal = 0

def get_money(input_string:str)->int:
    '''
    Получение суммы денег
    '''
    while True:
        try:
            num = int(input(input_string))
            if num > 0 and num % SUM_WORK == 0: 
                return num
            else:
                print('Сумма должна быть положительной и кратной 50')
        except ValueError:
            print('Это не то ...')

def refil_account(num:int):
    '''
    добавить деньги на счет
    '''
    global account
    account += num

def account_proc():
    '''
    добавление 3%
    '''
    global account
    num = account / 100 * COMM_REFIL
    refil_account(num)

def take_account(num:int):
    global account
    account -= num

def take_tax():
    global account
    if account > MAX_ACCAUNT:
        num = account / 100 * TAX
        take_account(num)

def chek_money(num):
    proc = num / 100 * COMM_WITHDRAWAL
    if proc < COMM_MIN:
        num += COMM_MIN
    elif proc > COMM_MAX:
        num += COMM_MAX
    else:
        num += proc
    return num

print('Здравствуйте.Это программа банкомат\n')
while True:
    choice = int(input('Выберите желаемое действие:\n'\
      '1 - Пополнить счет\n'\
      '2 - Снять деньги со счета\n'\
      '3 - Выход\n'))
    match choice:
        case 1:
            number = get_money('Введите сумму для зачисления на счет:\n')
            take_tax()
            refil_account(number)
            count_refil += 1
            if count_refil == 3:
                account_proc()
                count_refil = 0
            print(f'У вас на счету: {account} рублей')
        case 2:
            number = get_money('Введите сумму для снятия со счета:\n')
            take_tax()
            number = chek_money(number)
            if number < account:
                take_account(number)
                count_withdrawal += 1
                if count_withdrawal == 3:
                    account_proc()
                    count_withdrawal = 0
            else:
                print('Недостаточно средств')
            print(f'У вас на счету: {account} рублей')
        case 3:
            print('До свидания')
            print(f'У вас на счету: {account} рублей')
            break
        case _:
            print('Это не то ...')