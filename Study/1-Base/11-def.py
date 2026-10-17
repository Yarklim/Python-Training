def cube(value):
    if isinstance(value, (int, float)):
        return value**3

    return 'Value is not a number'


def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


print(cube(3))  # 27
print(cube('5'))  # 'Value is not a number'
print(is_number('123'))  # True
print(is_number('abc'))  # False


# ================= Позиционные и не позиционные параметры =================
def percent_of(value: int, part: int):
    if value <= 0 or part < 0:
        return False

    percent = part / value * 100
    return str(round(percent, 2)) + ' %'


result_1 = percent_of(100, 50)  # Позиционные аргументы
result_2 = percent_of(
    part=50, value=100
)  # Ключевые аргументы (с ключами). Но / (слеш) в параметрах функции запрещает передачу ключевых аргументов.

print(result_1)
print(result_2)


# ================= *args & **kwargs =================
def sum_all(*args) -> int:
    print(type(args))  # <class 'tuple'>
    print(args)  # (1, 2, 3, 4, 5)
    return sum(args)


result = sum_all(1, 2, 3, 4, 5)
print(result)  # Выведет: 15

# -----------------------------------


def print_user_info(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    for key, value in kwargs.items():
        print(f'{key}: {value}')


print_user_info(name='Yar', age=28, city='Kyiv')
# Выведет:
# name: Yar
# age: 28
# city: Kyiv


# ----------- комбинирование args и kwargs ------------
def complex_function(title, *args, status='active', **kwargs):
    print(f'Заголовок: {title}')
    print(f'Позиционные аргументы (args): {args}')
    print(f'Статус: {status}')
    print(f'Именованные аргументы (kwargs): {kwargs}')


complex_function('Отчет', 10, 20, 30, status='pending', author='Yar', year=2024)

# ----------- ** распаковывает словарь в именованные аргументы ------------
user_data_dict = {'name': 'Yar', 'age': 32}


def greet(name, age):
    print(f'Привет, {name}! Тебе {age} лет.')


greet(**user_data_dict)  # Эквивалентно greet(name="Yar", age=32)
