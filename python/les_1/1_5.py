proceeds = float(input("Введите выручку: "))
costs = float(input("Введите издержки: "))

if proceeds > costs:
    print(f"Фирма работает с прибылью. Рентабельность составляет: {proceeds / costs:.2f}")
    staff = int(input("Количество сотрудников фирмы состовляет: "))
    print(f"Прибыль в расчете на одного сторудника сотавила: {proceeds / staff:.2f}")
else:
    print("Фирма работает с убытком")