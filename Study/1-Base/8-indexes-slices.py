str = "hello"
print(str[1])  # e
print(str[-1])  # o
# print(str[10])  # ошибка!

# Slice
# Синтаксис срезов - скобки и три значения дапазона [start:stop:step] чкркз двлеточие
item = str[0:4]  # 'hell'
item_2 = str[2:]  # 'llo'


url = "https://www.google.com"
start_idx = url.index("www.") + 4
domain = url[start_idx:]  # google.com

negative_slice = url[-4:]  # .com
reverse_str = url[::-1]  # moc.elgoog.www//:sptth


str_2 = "C1, C2, C3, C4, C5"
some_str = str_2[::2]  # C,C,C,C,C
numbers_str = str_2[1::4]  # 12345

print(reverse_str)
