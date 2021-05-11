# 5-5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

user_num = input("Введите числа через пробел и нажмите Enter: ")

with open("file/file_les_5.txt", "w+") as f_obj: #файл на чтение и запись
    f_obj.writelines(user_num) #записываем построчно
    f_obj.seek(0)
    content = f_obj.read()
    list_num = content.split(' ')
    result = 0
    for el in list_num:
        result += int(el)
    print(result)
