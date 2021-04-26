def my_func(val_1, val_2, val_3):
    arguments = locals() #получаем аргументы
    result = {}
    my_sorted = sorted(arguments, key=arguments.get, reverse=True)
    for w in my_sorted:
        result[w] = arguments[w]

    # преобразоввываем в массив и выбрать два первых значения
    els = list(result.values())

    return f"Сумма наибольших равна: {els[0] + els[1]}"

print(my_func(5, 2, 3))