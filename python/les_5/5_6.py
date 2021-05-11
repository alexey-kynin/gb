# 5-6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
import re
result_dict = {}
with open("file/file_les_6.txt", "r", encoding="utf8") as f_obj:
    quantity = 0
    for line in f_obj:
        line_list = line.split(':')
        item_name = line_list[0]
        item_data = line_list[1].split()
        for el in item_data:
            quantity += int(re.findall('\d+', el)[0]) if len(re.findall('\d+', el)) > 0 else 0

        result_dict[item_name] = quantity

print(result_dict)