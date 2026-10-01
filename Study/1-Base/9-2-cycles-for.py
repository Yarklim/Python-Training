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

for i, item in enumerate(widgets, start=1):
    print(item.center(3), end='')

    if i % 3 == 0:
        print()

# ------------------------------------------------------------

tasks = ['Learn Python', 'Do homework', 'Read book', 'Buy food']
done = [False, True, False, True]

for task, status in zip(tasks, done):
    if status:
        mark = '[x]'
    else:
        mark = '[ ]'

    print(f'{mark} {task}')
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

# ------------ распаковка списка ------------
for i, j, k in widgets_2:
    print(i, end='')
    print(j, end='')
    print(k, end='')
    print()

# -------------------------------------------
country_codes = ['754', '690', '450']

products = [
    '4506436054267',
    '7547682958186',
    '6900626469201',
    '7543817559796',
    '7544194259711',
    '6900590565047',
    '6901237511586',
    '4502714135954',
    '4500295752923',
    '6901237511587',
]

categories = []

for country_code in country_codes:
    temp_list = []

    for product in products:
        code = product[:3:]

        if code == country_code:
            temp_list.append(product)

    categories.append(temp_list)

print(categories)
