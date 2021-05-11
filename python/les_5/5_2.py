
# 5-2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
import re

num_lin = 0
with open("file/file_les_2.txt", "r") as f_obj:
    for line in f_obj:
        num_lin += 1
        line = line.replace('  ', ' ') #как пример можно поудалять из строки двойные пробелы, и знаки припинания
        line = re.sub('[!?,]', '', line)

        word_count = len(line.split())
        print(f"Кол-во слов в {num_lin} строке равно: {word_count}")


print(f"Количество строк: {num_lin}")