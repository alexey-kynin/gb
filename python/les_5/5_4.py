
# 54. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

eng_num_list = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
ru_num_list = ['Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь', 'Девять']
ru_arr = []

with open("file/file_les_4.txt", "r", encoding="utf8") as f_obj:
    for line in f_obj:
        line = line.replace(' — ', ' ')

        line_arr = line.split()
        index_num = eng_num_list.index(line_arr[0])
        str_ru = ru_num_list[index_num] + ' - ' + line_arr[1]
        ru_arr.append(str_ru + '\n')

out_f = open("file/file_les_4_res.txt", "w")
out_f.writelines(ru_arr)
out_f.close()

