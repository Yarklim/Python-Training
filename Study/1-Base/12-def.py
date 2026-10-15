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
def percent_of(value, part):
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
