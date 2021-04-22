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
