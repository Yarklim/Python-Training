def cube(value):
    if isinstance(value, (int, float)):
        return value**3

    return 'Argument is not a number'


def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


print(cube(3))
print(cube('5'))
