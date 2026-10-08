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
