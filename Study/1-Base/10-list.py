list_1 = ["str1", 15, 6.2, "str2"]

print(list_1[1])  # 15
print(len(list_1))  # 4
print(15 in list_1)  # true
print(list(range(5)))

nums_list = [2, 5, 7, 1.8, 9, 36]
print(sum(nums_list))  # 60.8
print(min(nums_list))  # 1.8
print(max(nums_list))  # 36

nums_list.append(101)  # добавление элемента в конец
print(nums_list)  # [2, 5, 7, 1.8, 9, 36, 101]
print(sum(nums_list))  # 161.8
print(max(nums_list))  # 101

nums_list.insert(0, 55)  # добавление элемента в начало (или в указанный индекс)
print(nums_list)  # [55, 2, 5, 7, 1.8, 9, 36, 101]
print(sum(nums_list))  # 216.8

deleted_el = nums_list.pop(3)  # удаление элемента по индексу
print(deleted_el)  # 7
print(nums_list)  # [55, 2, 5, 1.8, 9, 36, 101]
print(sum(nums_list))  # 209.8

nums_list.remove(1.8)  # удаление элемента по значению
print(nums_list)  # [55, 2, 5, 9, 36, 101]

nums_list.sort()  # сортировка списка по возрастанию
print(nums_list)  # [55, 2, 5, 9, 36, 101]
nums_list.sort(reverse=True)  # сортировка списка по убыванию
print(nums_list)  # [101, 55, 36, 9, 5, 2]
str = "Python is a programming language"

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

languages = ["TS", "Python", "GO"]
for i, el in enumerate(languages):
    print(i, el)
# 0 TS
# 1 Python
# 2 GO

# ==================== Метода списка =======================


my_list = str.split()  # по умолчанию разделяет по пробелам
print(my_list)  # ['Python', 'is', 'a', 'programming', 'language']

ip = "127.0.0.1"
ip_list = ip.split(".")  # разделитель по точке
print(ip_list)  # ['127', '0', '0', '1']

ip_str = ".".join(ip_list)  # строка из списка, склеивает через "."
print(ip_str)  # 127.0.0.1
