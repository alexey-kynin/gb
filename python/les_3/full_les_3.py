# 3_1
num_one = int(input("Введите первое число: "))
num_two = int(input("Введите второе число: "))


def my_div(num_one, num_two):
    if num_two == 0:
        return 'На ноль делить нельзя!'
    return num_one/num_two


result = my_div(num_one, num_two)
print(f"результат: {result}")

# 3_2

# Первый вариант. просто "поиграться" с методом  **kwargs и словарем, и так же не зависим от кол-ва вводимых параметров:
space = ' '
res_line = ''


def user_data(**kwargs):
    return kwargs


result_user_data = user_data(user_name='Alexey', user_year_birth='1988', user_city='Barnaul', user_email='qwer@mail.ru', user_telephone='123456789')

for val in result_user_data:
    res_line = res_line + result_user_data[val] + space

print(res_line)


# Второй вариант: получаем строку в функции

def user_data_two(user_name, user_year_birth, user_city, user_email, user_telephone):
    arguments = locals()
    res_line_two = ''
    for val in arguments:
        res_line_two = res_line_two + result_user_data[val] + space

    return res_line_two

result_user_data_two = user_data_two(user_name='Alexey', user_year_birth='1988', user_city='Barnaul', user_email='qwer@mail.ru', user_telephone='123456789')

print(result_user_data_two)

#3_3
def my_func(val_1, val_2, val_3):
    arguments = locals() #получаем аргументы
    result = {}
    my_sorted = sorted(arguments, key=arguments.get, reverse=True)
    for w in my_sorted:
        result[w] = arguments[w]

    # преобразоввываем в массив и выбрать два первых значения
    els = list(result.values())

    return f"Сумма наибольших равна: {els[0] + els[1]}"

print(my_func(5, 2, 3))

#3_4
def my_func(x, y):
    i = 1
    result = x
    while i < abs(y):
        result *= x
        i += 1

    return f"{x} в степени {abs(y)} равен: {result}"

print(my_func(4, -3))

#3_5

sp_char = '%' #спец символ

def summation_func(res_sum = 0):
    user_num = input("Введите числа через пробел и нажмите Enter: ")

    res_num = user_num.split(' ') # получаем массив

    try:
        index = res_num.index(sp_char) #если есть символ и его индекс больше 0 то добавим к сумме цифры ДО спец символа
        if index > 0:
            res = 0
            for val in res_num[:index]:
                res += int(val)
        return res_sum +  res
    except ValueError: #если нет sp_char в "листе" то просто суммируем все числа приведя их к числу перед сложением
        for val in res_num:
            res_sum += int(val)
        return summation_func(res_sum) #и вызовем функцию еще раз


print(summation_func())

#3_6

user_text = 'if all you need to know'
res_test = ''

def int_func(say = ''):
    return say.title()

for val in user_text.split(' '):
    res_test += int_func(val) + " "

print(res_test)