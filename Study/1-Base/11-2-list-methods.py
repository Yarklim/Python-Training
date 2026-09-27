# ==================== Методы списка =======================
# nums_list = [2, 5, 7, 1.8, 9, 36]

# nums_list.append(101)  # добавление элемента в конец
# print(nums_list)  # [2, 5, 7, 1.8, 9, 36, 101]
# print(sum(nums_list))  # 161.8
# print(max(nums_list))  # 101

# additional_nums = [16, 17]

# nums_list.extend(
#     additional_nums
# )  # [2, 5, 7, 1.8, 9, 36, 101, 16, 17] - добавляет элементы из итерируемого объекта в конец списка

# nums_list.insert(0, 55)  # добавление элемента в начало (или в указанный индекс)
# print(nums_list)  # [55, 2, 5, 7, 1.8, 9, 36, 101]
# print(sum(nums_list))  # 216.8

# deleted_el = nums_list.pop(3)  # удаление элемента по индексу
# print(deleted_el)  # 7
# print(nums_list)  # [55, 2, 5, 1.8, 9, 36, 101]
# print(sum(nums_list))  # 209.8

# nums_list.remove(1.8)  # удаление элемента по значению
# print(nums_list)  # [55, 2, 5, 9, 36, 101]

# nums_list.index(
#     101
# )  # 5 - возвращает индекс первого вхождения элемента, генерирует ошибку, если элемент не найден

# nums_list.sort()  # сортировка списка по возрастанию
# print(nums_list)  # [55, 2, 5, 9, 36, 101]

# nums_list.sort(reverse=True)  # сортировка списка по убыванию
# print(nums_list)  # [101, 55, 36, 9, 5, 2]

# nums_list.reverse()  # список в обратном порядке
# print(nums_list)  # [101, 36, 9, 5 , 2, 55]

# numbers_list = [1, 4, 5, 6, 4]

# copy_list = numbers_list.copy()  # [1, 4, 5, 6, 4] - создает копию списка

# copy_list.clear()  # [] - удаляет все элементы из списка

# numbers_list.count(4)  # 2 - возвращает количество вхождений элемента в список

# str = 'Python is a programming language'
# my_list = str.split()  # по умолчанию разделяет по пробелам
# print(my_list)  # ['Python', 'is', 'a', 'programming', 'language']

# ip = '127.0.0.1'
# ip_list = ip.split('.')  # разделитель по точке
# print(ip_list)  # ['127', '0', '0', '1']

# ip_str = '.'.join(ip_list)  # строка из списка, склеивает через "."
# print(ip_str)  # 127.0.0.1

# ======================= Каскадное применение методов ========================
scraped_prices = ['100,50', '5,80', '', '', '25,99', '', '17,50', '0,95', '99,00']

normalized_price_lst = []

i = 0

while i < len(scraped_prices):
    item = scraped_prices[i]

    if item:
        item = float(item.replace(',', '.'))
        normalized_price_lst.append(item)

    i += 1


print(normalized_price_lst)
