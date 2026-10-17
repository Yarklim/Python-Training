# ================== Dictionary ===================

car = {'model': 'Mersedes', 'year': 2024, 'color': 'silver'}

print(car)

print('My car model:', car['model'])  # Если значения нет - выведется ошибка!
print('My car color:', car.get('color'))  # Если значения нет - выведется None
print(
    'My car color:', car.get('abc', 'black')
)  # Если значения нет - выведется значение по дефолту ('black')

car['year'] = 2025
car['is_use'] = True

print(car)

# --------------------- Итерация словаря ---------------------------
# Вывод ключей словаря:
for key in car:
    print(key)
# или:
print(list(car.keys()))

# Вывод значений ключей словаря:
for value in car.values():
    print(value)
# или:
print(list(car.values()))

# Вывод пар ключ-значение:
for key, value in car.items():
    print(f'{key}, {value}')
# или:
print(
    list(car.items())
)  # [('model', 'Mersedes'), ('year', 2025), ('color', 'silver'), ('is_use', True)] - список кортежей
