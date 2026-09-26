list_1 = ['str1', 15, 6.2, 'str2']

print(list_1[1])  # 15
print(len(list_1))  # 4
print(15 in list_1)  # true
print(list(range(5)))

list_2 = [1, 2, 3, 4]
print(list_2)  # [1, 2, 3, 4]
print(id(list_2))  # 4654378164224
list_2 = list_2 + [5, 6, 7]  # Получим новый список!
print(list_2)  # [1, 2, 3, 4, 5, 6, 7]
print(id(list_2))  # 4654378160704
list_2 += [8, 9, 10]  # В сокращенной форме записи расширится старый список!
print(list_2)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(id(list_2))  # 4654378160704

nums_list = [2, 5, 7, 1.8, 9, 36]
print(sum(nums_list))  # 60.8
print(min(nums_list))  # 1.8
print(max(nums_list))  # 36

all_nums_list = [i for i in range(5)]  # заполняется числами от 0 до 4 (индексы)
print(all_nums_list)  # [0, 1, 2, 3, 4]

even_nums_list = [
    i for i in range(13) if (i % 2) == 0
]  # заполняется четными числами от 0 до 12 (индексы)
print(even_nums_list)  # [0, 2, 4, 6, 8, 10, 12]

# ===================== Иттерация списка =======================
numbers = [4, 6, 98, 45]
for i in numbers:
    print(i)

languages = ['TS', 'Python', 'GO']
for i, el in enumerate(languages):
    print(i, el)
# 0 TS
# 1 Python
# 2 GO
