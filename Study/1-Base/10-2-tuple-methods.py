# ======================= Методы кортежа =========================

data = ('Home', 'Catalog', 'Payment & Shipping', 'About')

apartments = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

print(apartments[1::2])  # (2, 4, 6, 8, 10)
print(data[1])  # 'Catalog'

vertabrae = (
    'C1',
    'C2',
    'C3',
    'C4',
    'C5',
    'C6',
    'C7',
    'T1',
    'T2',
    'T3',
    'T4',
    'T5',
    'T6',
    'T7',
    'T8',
    'T9',
    'T10',
    'T11',
    'T12',
)

target_slice = vertabrae[vertabrae.index('T1') : len(vertabrae)]

s = '-'.join(vertabrae)  # join только строк, автоматически не конвертирует

print(vertabrae.count('C5'))  # 1
print(
    target_slice
)  # ('T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12')
print(bool(vertabrae))  # True
print(
    str(vertabrae)
)  # Строка '('C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12')'
print(s)  # 'C1-C2-C3-C4-C5-C6-C7-T1-T2-T3-T4-T5-T6-T7-T8-T9-T10-T11-T12'

# ------------------------------------------------------------
temps = (12, 15, 14, 10, 9, 11, 13)  # кортежи одинаковой длины.
week = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

# Код тут.
i = 0

while i < len(temps):
    print(f'{week[i]}: {temps[i]} °C')

    i += 1

# -----------------------------------------------------------
month = (
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
)

week_days = (
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
)
first = 'Wednesday'  # День недели первого числа.

first_index = week_days.index(first)
