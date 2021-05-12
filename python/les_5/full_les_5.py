# 5-1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

user_str_arr = []
while True:
    user_str = input("Введите строку: ")
    if len(user_str) > 0:
        user_str_arr.append(user_str + '\n')
    else:
        break

with open("file/file_les_1.txt", "w") as f_obj:
    f_obj.writelines(user_str_arr)

# 5-2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
import re

num_lin = 0
with open("file/file_les_2.txt", "r") as f_obj:
    for line in f_obj:
        num_lin += 1
        line = line.replace('  ', ' ')  # как пример можно поудалять из строки двойные пробелы, и знаки припинания
        line = re.sub('[!?,]', '', line)

        word_count = len(line.split())
        print(f"Кол-во слов в {num_lin} строке равно: {word_count}")

print(f"Количество строк: {num_lin}")

# 5-3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

# мой пример файла:
# Иванов 14400
# Петров 23000
# Сидоров 12000
# Ельцин 42000

num_lin = 0
threshold = 20000
employee_names = ''
sum_staff_salary = 0
with open("file/file_les_3.txt", "r", encoding="utf8") as f_obj:
    for line in f_obj:
        num_lin += 1  # Сичтаем строки, или кол-во сотрудников
        staff_data = line.split()  # Разбиваем по пробелу, подразумевая что файл имеет некий стандарт заполнения "Петров 23000"
        staff_name = staff_data[0]
        staff_salary = int(staff_data[1])

        sum_staff_salary += staff_salary
        if staff_salary > threshold:
            employee_names += staff_name + ' '

average_salary = sum_staff_salary / num_lin
print(f"У сотрулников: {employee_names}оклад больше {threshold}")
print(f"Всего работает {num_lin} сотрудников/а. Сумма оклада: {sum_staff_salary}. Средний доход: {average_salary}")

# 54. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

eng_num_list = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
ru_num_list = ['Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь', 'Девять']
ru_arr = []

with open("file/file_les_4.txt", "r", encoding="utf8") as f_obj:
    for line in f_obj:
        line = line.replace(' — ', ' ')

        line_arr = line.split()
        index_num = eng_num_list.index(line_arr[0])
        str_ru = ru_num_list[index_num] + ' - ' + line_arr[1]
        ru_arr.append(str_ru + '\n')

out_f = open("file/file_les_4_res.txt", "w")
out_f.writelines(ru_arr)
out_f.close()

# 5-5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

user_num = input("Введите числа через пробел и нажмите Enter: ")

with open("file/file_les_5.txt", "w+") as f_obj:  # файл на чтение и запись
    f_obj.writelines(user_num)  # записываем построчно
    f_obj.seek(0)
    content = f_obj.read()
    list_num = content.split(' ')
    result = 0
    for el in list_num:
        result += int(el)
    print(result)

# 5-6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
import re

result_dict = {}
with open("file/file_les_6.txt", "r", encoding="utf8") as f_obj:
    quantity = 0
    for line in f_obj:
        line_list = line.split(':')
        item_name = line_list[0]
        item_data = line_list[1].split()
        for el in item_data:
            quantity += int(re.findall('\d+', el)[0]) if len(re.findall('\d+', el)) > 0 else 0

        result_dict[item_name] = quantity

print(result_dict)

# 5-7
import json

average_profit = 0
firm_dict = {}
result_list = []
with open("file/file_les_7.txt", "r", encoding="utf8") as f_obj:
    for line in f_obj:
        line_list = line.split()
        firm_name = line_list[0]
        firm_own = line_list[1]
        firm_proceeds = int(line_list[2])
        firm_costs = int(line_list[3])

        firm_profit = firm_proceeds - firm_costs

        if firm_profit >= 0:
            average_profit += firm_profit
            firm_dict[firm_name] = firm_profit
        else:
            average_profit += 0

    average_profit_dict = dict(average_profit=average_profit)

    result_list.append(firm_dict)
    result_list.append(average_profit_dict)

    print(json.dumps(result_list))


