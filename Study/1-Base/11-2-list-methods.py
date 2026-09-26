# ==================== Методы списка =======================
nums_list = [2, 5, 7, 1.8, 9, 36]

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

str = 'Python is a programming language'
my_list = str.split()  # по умолчанию разделяет по пробелам
print(my_list)  # ['Python', 'is', 'a', 'programming', 'language']

ip = '127.0.0.1'
ip_list = ip.split('.')  # разделитель по точке
print(ip_list)  # ['127', '0', '0', '1']

ip_str = '.'.join(ip_list)  # строка из списка, склеивает через "."
print(ip_str)  # 127.0.0.1
