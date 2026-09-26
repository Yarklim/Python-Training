# ======================= Методы кортежа =========================

data = ('Home', 'Catalog', 'Payment & Shipping', 'About')

apartments = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

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
