user_month = int(input("Введите месяц в виде целого числа от 1 до 12: "))

months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

winter = [0, 1, 11]
spring = [2, 3, 4]
summer = [5, 6, 7]
autumn = [8, 9, 10]
yea = [winter, spring, summer, autumn]
yea_str = ['зимний', 'веснний', 'летний', 'осенний']
user_month = user_month - 1

for idx, val in enumerate(yea):
    if user_month in val:
        print(f"{months[user_month]} {yea_str[idx]} месяц")
