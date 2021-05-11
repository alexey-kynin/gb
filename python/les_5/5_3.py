
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
        num_lin += 1 #Сичтаем строки, или кол-во сотрудников
        staff_data = line.split() #Разбиваем по пробелу, подразумевая что файл имеет некий стандарт заполнения "Петров 23000"
        staff_name = staff_data[0]
        staff_salary = int(staff_data[1])

        sum_staff_salary += staff_salary
        if staff_salary > threshold:
            employee_names += staff_name + ' '

average_salary = sum_staff_salary/num_lin
print(f"У сотрулников: {employee_names}оклад больше {threshold}")
print(f"Всего работает {num_lin} сотрудников/а. Сумма оклада: {sum_staff_salary}. Средний доход: {average_salary}")
