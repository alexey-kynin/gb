# 1_1
# Создаем переменные и выводим на экран
a = 1
b = 2.4
c = "Алексей"
print(c)
name = input("результат сложения a и b: " + str(a + b))

# Запросим числа и выведим результат
q = int(input("Введите первое число: "))
w = int(input("Введите второе число: "))
e = input("Кто вводил данные: ")
s = q + w
print(f"Получаем:  {str(s)}, ввел:  {e}")

# 1_2
# Вариант 1:
import datetime

sec = int(input("Введите кол-во секунд: "))

time = str(datetime.timedelta(seconds=sec))
print(time)

# Вариант 2: Использую тернарный оператор (можно использовать if), так же арифмитические операторы. и вывод с помощью форматирования f-строкой
sec_user = int(input("Введите кол-во секунд: "))
sec_h = 3600
sec_m = 60

hour = sec_user // sec_h
hour = (str(hour), "0" + str(hour))[hour < 10]

minute = (sec_user % sec_h) // 60
minute = (str(minute), "0" + str(minute))[minute < 10]

sec = (sec_user % sec_h) % 60
sec = (str(sec), "0" + str(sec))[sec < 10]

print(f"Получаем:  {str(sec_user)} секунд. Выводим:  {str(hour)}:{str(minute)}:{sec}")


# 1_3
a = int(input("Введите число n: "))
s = (a + int(str(a) + str(a)) + int(str(a) + str(a) + str(a)))
print(f"n + nn + nnn = {s}")

# 1_4
a = input("Введите целое положительное число n: ")

# Можно сделать некоторые проверки на то что ввел нам польщователь. для примера проверка на "целое" число
if not float(a).is_integer():
    print("Вы не ввели целое положительное число!")
else:
    a = abs(int(a))

    res = a % 10
    if res == 9:
        print("Самая большая цифра в числе ", res)
        exit()
    else:
        a = a // 10
        while a >= 1:
            a = a // 10
            if a % 10 > res:
                res = a % 10
            if a > 9:
                continue
            else:
                print("Самая большая цифра в числе ", res)
                break


# 1_5
proceeds = float(input("Введите выручку: "))
costs = float(input("Введите издержки: "))

if proceeds > costs:
    print(f"Фирма работает с прибылью. Рентабельность составляет: {proceeds / costs:.2f}")
    staff = int(input("Количество сотрудников фирмы состовляет: "))
    print(f"Прибыль в расчете на одного сторудника сотавила: {proceeds / staff:.2f}")
else:
    print("Фирма работает с убытком")

# 1_6
a = abs(int(input("Введите начальный км: ")))
b = abs(int(input("Введите конечный км: ")))
i = 1

while a<=b:
    i = i + 1
    a = a  + a/10

print(f"Ответ: на {i}-й день спортсмен достиг результата — не менее {b} км.")