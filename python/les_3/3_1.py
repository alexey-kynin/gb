num_one = int(input("Введите первое число: "))
num_two = int(input("Введите второе число: "))


def my_div(num_one, num_two):
    if num_two == 0:
        return 'На ноль делить нельзя!'
    return num_one/num_two


result = my_div(num_one, num_two)
print(f"результат: {result}")