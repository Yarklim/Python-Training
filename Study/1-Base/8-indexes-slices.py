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


str_2 = "C1, C2, C3, C4, C5, C6, C7"
some_str = str_2[::2]  # C,C,C,C,C
numbers_str = str_2[1::4]  # 12345

mask = "i_t_s_ _a_ _s_e_c_r_e_t_ _w_o_r_d"

real = mask[::2]

print(real)

print(reverse_str)
