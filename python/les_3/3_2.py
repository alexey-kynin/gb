
# Первый вариант. просто "поиграться" с методом  **kwargs и словарем, и так же не зависим от кол-ва вводимых параметров:
space = ' '
res_line = ''


def user_data(**kwargs):
    return kwargs


result_user_data = user_data(user_name='Alexey', user_year_birth='1988', user_city='Barnaul', user_email='qwer@mail.ru', user_telephone='123456789')

for val in result_user_data:
    res_line = res_line + result_user_data[val] + space

print(res_line)


# Второй вариант: получаем строку в функции

def user_data_two(user_name, user_year_birth, user_city, user_email, user_telephone):
    arguments = locals()
    res_line_two = ''
    for val in arguments:
        res_line_two = res_line_two + result_user_data[val] + space

    return res_line_two

result_user_data_two = user_data_two(user_name='Alexey', user_year_birth='1988', user_city='Barnaul', user_email='qwer@mail.ru', user_telephone='123456789')

print(result_user_data_two)