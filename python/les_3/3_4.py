def my_func(x, y):
    i = 1
    result = x
    while i < abs(y):
        result *= x
        i += 1

    return f"{x} в степени {abs(y)} равен: {result}"

print(my_func(4, -3))