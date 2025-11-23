# +x, -x, ~x - Инверсия знака, побитовая инверсия (~x)
# *, @, /, //, % - Умножение, матричное умножение, деление, целочисленное деление, остаток от целочисленного деления
# <<, >> - Побитовые сдвиги
# & - "И"
# ^ - "Исключающее ИЛИ"
# | - "ИЛИ"
# in, not in, is, is not, <, <=, >=, !=, == - Сравнения
# not x - Логическое "НЕ"
# and - Логическое "И"
# or - Логическое "ИЛИ"
# =, +=, -=, *=, /=, //=, %=, **=, := - Присваивание, моржовый оператор (:=)

import math

num_tickets = 237  # количество проданных билетов
bus_capacity = 48  # количество мест в автобусе

num_bus = num_tickets // bus_capacity
num_left_passengers = num_tickets % bus_capacity

print(num_bus, num_left_passengers)

x = 237 / 48

res_1 = round(x)
res_2 = round(x, 2)
res_3 = math.ceil(x)
res_4 = math.floor(x)

print(res_1)
print(res_2)
print(res_3)
print(res_4)
