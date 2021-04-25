user_month = int(input("Введите месяц в виде целого числа от 1 до 12: "))

yea = {'зимний': {1: 'январь', 2: 'февраль', 12: 'декабрь'},
       'веснний': {3: 'март', 4: 'апрель', 5: 'май'},
       'летний': {6: 'июнь', 7: 'июль', 8: 'август'},
       'осенний': {9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь'}
       }

for season in yea:
    for month in yea[season]:
        if month == user_month:
            print(f"{yea[season][month]} {season} месяц")
