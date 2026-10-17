# ============= Tuple ==============
# Кортеж - неизменяемый тип данных (елементы нельзя изменить или добавить/удалить)
# Но изменяемый тип данных, который лежит в кортеже, изменить можно - data = (1, 2, [3, 4]) (список [3, 4] можно изменить)

data_1 = tuple('hello')  # ('h', 'e', 'l', 'l', 'o')
data_2 = (5, 6, -34, 'hello', True)  # (5, 6, -34, 'hello', True)
x = (1,)  # (1,)

# --------------------------------------
# Можно добавить новый элемент, но это будет уже другой кортеж!
new_data = ('JS', 'TS', 'Python')

print(new_data)  # ('JS', 'TS', 'Python')
print(id(new_data))  # 4071636840032

new_data = new_data + ('GO',)

print(new_data)  # ('JS', 'TS', 'Python', 'GO')
print(id(new_data))  # 4071636840272

# --------------------------------------
red = (255, 0, 0)
green = (0, 255, 0)

# --------------------------------------
resolution = (1920, 1080)

width, height = resolution  # распаковка переменных

print(width)  # 1920
print(height)  # 1080


# --------------------------------------
def get_user():
    return 'John', 42


name, age = get_user()

print(name)  # John
print(age)  # 42


# *args внутри функции — это tuple
def print_numbers(*numbers):
    print(numbers)
    print(type(numbers))


print_numbers(10, 20, 30)  # (10, 20, 30) <class 'tuple'>

# --------------------------------------
# Кортеж можно использовать как ключ, если его элементы hashable:
# Можно: key = (1, 2, 'hello')
# Нельзя: key = (1, [2, 3]) (Потому что внутри находится изменяемый list)

board = {
    (0, 0): 'A',
    (0, 1): 'B',
    (1, 0): 'C',
}

# --------------------------------------
# tuple можно положить в set.
# Например, мы обходим двумерное поле и храним уже посещённые координаты:
visited = {
    (1, 2),
    (3, 4),
    (5, 6),
}

visited = set()

position = (3, 5)

visited.add(position)

if (3, 5) in visited:
    print('Уже посещали')

# --------------------------------------
# Распаковка, упаковка и множественное присваивание переменных.

date = (15, 'March', 1972)

day, month, year = date  # Unpacking

day, *other = date  # * - packing

day, month, year = 15, 'March', 1972  # Множественное присваивание

print(f'{day} {month}, {year}')  # 15 March, 1972
print(other)  # ['March', 1972]
