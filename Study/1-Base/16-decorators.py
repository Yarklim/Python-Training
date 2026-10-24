# ==================== Декораторы ======================

# Декоратор - это функция, которая принимает другую функцию в качестве аргумента, добавляет к ней некоторую функциональность
# или логику и возвращает изменённую или новую функцию, не меняя при этом исходный код обёрнутой функции.

# В основе декораторов лежит концепция того, что функции являются объектами первого класса (First-Class Objects) -
# их можно передавать в качестве аргументов, возвращать из других функций и присваивать переменным.

import time
from functools import wraps


def timer_decorator(func):
    """Декоратор для измерения времени выполнения функции."""

    @wraps(func)  # Сохраняет __name__ и __doc__ исходной функции
    def wrapper(*args, **kwargs):
        start_time = time.time()

        # Вызов оригинальной функции
        result = func(*args, **kwargs)

        execution_time = time.time() - start_time
        print(f'Функция {func.__name__} выполнилась за {execution_time:.4f} сек.')

        # Возвращаю результат оригинальной функции
        return result

    return wrapper


# Применение декоратора
@timer_decorator
def heavy_computation(n):
    return sum(i * i for i in range(n))


# Вызов
res = heavy_computation(10_000_000)
# Выведет: Функция heavy_computation выполнилась за 0.3541 сек.


# --------------- Декораторы, принимающие аргументы ---------------
def repeat(num_times):
    """Декоратор, повторяющий выполнение функции N раз."""

    def decorator_repeat(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator_repeat


@repeat(num_times=3)
def say_hello():
    print('Привет!')


say_hello()
# Выведет "Привет!" три раза


# -------------- Декоратор на основе класса --------------
class CountCalls:
    """Декоратор-класс, считающий количество вызовов функции."""

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'Функция {self.func.__name__} вызвана {self.num_calls} раз(а)')
        return self.func(*args, **kwargs)


@CountCalls
def say_hi():
    print('Привет!')


say_hi()  # Функция say_hi вызвана 1 раз(а)
say_hi()  # Функция say_hi вызвана 2 раз(а)
