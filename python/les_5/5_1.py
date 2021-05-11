# 5-1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

user_str_arr = []
while True:
    user_str = input("Введите строку: ")
    if len(user_str) > 0:
        user_str_arr.append(user_str+'\n')
    else:
        break

with open("file/file_les_1.txt", "w") as f_obj:
    f_obj.writelines(user_str_arr)
