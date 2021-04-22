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