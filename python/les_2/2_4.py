# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.


my_str = input("Введите строку из нескольких слов, разделённых пробелами: ")
str_arr = my_str.split(' ')
num = 1
for val in str_arr:
    print(f"{num}: {val}")
    num += 1 