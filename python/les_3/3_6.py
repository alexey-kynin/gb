
user_text = 'if all you need to know'
res_test = ''

def int_func(say = ''):
    return say.title()

for val in user_text.split(' '):
    res_test += int_func(val) + " "

print(res_test)