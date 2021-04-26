
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