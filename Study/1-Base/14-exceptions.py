# =============== Исключения =================
try:
    result = 10 / 0
except ZeroDivisionError:
    print('Ошибка: деление на ноль!')

# Выведет: Ошибка: деление на ноль!

# -------------------- ValueError (Некорректное значение) -------------------------
try:
    number = int('привет')
except ValueError as e:
    print(f'Перехвачено исключение: {e}')
    # Выведет подробности ошибки от Python

# -------------------- KeyError (Ошибка ключа) -------------------------
user = {'name': 'Алексей', 'age': 30}

try:
    print(user['email'])
except KeyError:
    print('Такого ключа в словаре нет!')

# -------------------- FileNotFoundError (Файл не найден) -------------------------
try:
    with open('non_existent_file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print('Указанный файл не найден. Проверьте путь.')

# --------------------- Обработка нескольких исключений ------------------------
try:
    # Какой-то ввод от пользователя
    user_input = input('Введите число: ')
    number = 100 / int(user_input)
except (ZeroDivisionError, ValueError) as e:
    print(f'Произошла ошибка! Тип: {type(e).__name__}, Описание: {e}')

# --------------------- Полная конструкция: else и finally ------------------------
try:
    with open('data.txt', 'w', encoding='utf-8') as file:
        file.write('Привет, мир!')
except OSError as e:
    print(f'Ошибка при работе с файлом: {e}')
else:
    print('Запись в файл прошла успешно!')
finally:
    # Здесь не нужно вручную закрывать файл - с этим справился с сам 'with'.
    # Этот блок используется для других финальных действий.
    print('Завершение работы программы.')


# --------------------- Принудительный вызов исключения (raise) ------------------------
def set_age(age):
    if age < 0 or age > 120:
        raise ValueError('Возраст должен быть в пределах от 0 до 120 лет.')
    print(f'Возраст успешно установлен: {age}')


try:
    set_age(150)
except ValueError as e:
    print(f'Ошибка валидации: {e}')
