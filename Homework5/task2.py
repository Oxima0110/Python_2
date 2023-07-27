# Напишите однострочный генератор словаря, который принимает 
# на вход три списка одинаковой длины: имена str, ставка int, 
# премия str с указанием процентов вида «10.25%». В результате 
# получаем словарь с именем в качестве ключа и суммой 
# премии в качестве значения. Сумма рассчитывается 
# как ставка умноженная на процент премии 


def dict_awards(names:list[str], money:list[int|float], bonus:list[str])->dict[str:float]:
    yield {name:salary/100 *bon for name, salary, bon in 
            zip(names, money, (float(i[:-1]) for i in bonus))}


list_name = ['Иван', 'Олег', 'Василий', 'Петр']
list_money = [125000, 110000, 118000, 130000]
list_bonus = ['10.22%', '12.3%', '8.5%', '9.85%']

print(*dict_awards(list_name, list_money, list_bonus))