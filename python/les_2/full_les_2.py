# 2_1
user_list = ['Првиет!', 33, 5.6, None ]
print(user_list)
for el in user_list:
    print(f"Элемент: '{el}' имеет тип: {type(el)}")

# 2_2
count_list = int(input("Введите кол-во элементов: "))
print('Вводите элементы в массив, нажимайте enter')

list = []
for i in range(count_list):
    list.append(input())

print(f"Исходный список: {list}")

result_list = []
count = len(list)

for idx, val in enumerate(list): #начинаем перебирать список
    if (idx % 2 == 0): # четный индекс мы увиличиваем на 1
        idx_res = idx + 1
        if idx_res <= count-1: # важно отследить получения индекса больше чем в исходном листе
            result_list.insert(idx_res, list[idx])
        else:
            result_list.insert(idx, list[idx])
    else: # НЕ четный индекс мы уменьшаем на 1
        idx_res = idx - 1
        if idx_res >= 0:
            result_list.insert(idx_res, list[idx])

print(f"Измененный списко: {result_list}")

# 2_3
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

# 2_3_v2
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

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.


my_str = input("Введите строку из нескольких слов, разделённых пробелами: ")
str_arr = my_str.split(' ')
num = 1
for val in str_arr:
    print(f"{num}: {val}")
    num += 1

# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

user_num = int(input("Введите новый элемент рейтинга: "))
my_list = [7, 5, 3, 3, 2]

for idx, val in enumerate(my_list):
    if user_num == val:
        print(idx)
        my_list.insert(idx, user_num)
        break
    else:
        my_list.insert(0, user_num)
        break

my_list.sort(reverse=True)
print(my_list)
