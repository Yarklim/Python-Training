# =============== FOR ===============
# --------- loop statements ----------
"""
for i in expression:
    if expression:
        continue # пропускает текущую итерацию
    elif expression:
        break # прерывает выполнение цикла

    expression or statement

else:
    expression or statement # выполняется, если цикл не прервался
"""

# ------------------------------------------------------------

for i in range(3):
    print(i, 'Hello')

# ---- от и до ----
for i in range(2, 5):
    print(i, 'Hello')

# ---- от и до с шагом ----
for i in range(1, 7, 2):
    print(i, 'Hello')


# ------------------------------------------------------------

widgets = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '*',
    '0',
    '#',
]

for count, item in enumerate(widgets, start=1):
    print(item.center(3), end='')

    if count % 3 == 0:
        print()

# ------------------------------------------------------------

scraped_prices = [
    '100,50',
    '5,80',
    '',
    '',
    '25,99',
    '25,99',
    '',
    '17,50',
    '0,95',
    '99,00',
]
new = []

for item in scraped_prices:
    if not item:
        continue

    if not item.replace(',', '').isdigit():
        new.clear()
        print('Error data')
        break

    item = float(item.replace(',', '.'))

    if not item in new:
        new.append(item)

print(new)

# ================ FOR вложенный в FOR =================

widgets_2 = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#'],
]

for block in widgets_2:
    for item in block:
        print(item.center(3), end='')
    print()
