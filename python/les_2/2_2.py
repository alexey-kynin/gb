count_list = int(input("Введите кол-во элементов: "))
print('Вводите элементы в массив, нажимайте enter')

list = []
for i in range(count_list):
    list.append(input())

print(f"Исходный список: {list}")

result_list = []
count = len(list)

for idx, val in enumerate(list): #начинаем перебирать список
    if (idx % 2 == 0): # четный индекс мы увиличиваем на 1
        idx_res = idx + 1
        if idx_res <= count-1: # важно отследить получения индекса больше чем в исходном листе
            result_list.insert(idx_res, list[idx])
        else:
            result_list.insert(idx, list[idx])
    else: # НЕ четный индекс мы уменьшаем на 1
        idx_res = idx - 1
        if idx_res >= 0:
            result_list.insert(idx_res, list[idx])

print(f"Измененный списко: {result_list}")


