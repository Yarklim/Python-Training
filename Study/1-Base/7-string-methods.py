user_input = 'Hello'
word = 'hello'
greeting = 'hi therE!'
toReplace = 'Hi Bob! Hi Mary!'

print(user_input[1])  # 'e'
print(user_input[-1])  # 'o'

len(word)  # 5

newGretting = greeting.capitalize()  # 'Hi there!'
newStr1 = user_input.lower()  # В нижний регистр
newStr2 = user_input.casefold()  # В нижний регистр (делает оптимизацию сравнения строк)
newStr3 = user_input.upper()  # В верхний регистр
new_user_input = user_input.strip()  # Очищает пробелы в начале и в конце строки
print(greeting.startswith('hi'))  # true
print(toReplace.startswith('hi'))  # false
print(greeting.endswith('!'))  # true
print(toReplace.endswith('?'))  # false
count = greeting.count('h')  # 2 - Количество вхождений подстроки 'h' в строку
replaced1 = toReplace.replace('Hi', 'Goodbay')  # Заменит все вхождения 'Hi' в строке
replaced2 = toReplace.replace(
    'Hi', 'Goodbay', count=1
)  # Заменит первое вхождение 'Hi' в строке

# ====================================================
# Список методов есть в шпаргалке!
# ====================================================

# =============== Литералы строк ===============
x1 = 'Hello ' + 'World!'  # 'Hello World'
x2 = """
Hello
"""  # многострочный вывод
x3 = r'C:\\Users\name\Desctop'  # литерал r, чтобы \n не перенес строку

# =============== Форматирование строк ===============
name = 'Yar'
rating = 4.95124
# greeting2 = 'Hello {}, your rating is: {}'.format(name, rating)
greeting2 = f'User name: {name} | User rating: {rating:.2f}'  # User name: Yar | User rating: 4.95

print(greeting2)

# Список стран (НЕ МЕНЯТЬ ЕГО тут, у себя на ПК можно менять):
raw_names = [
    'peru',
    'cANADA',
    'australia',
    'austria',
    'slovenia',
    'slovakia',
    'sweden',
    'switzerland',
    'new zealand',
    'uae',
    'usa',
]

# ----------------------------------------------------------------
# Нужно в список normalized_names записать эти названия согласно
# правилам написания: Peru, Canada, New Zealand, USA  <- пример
normalized_names = []
# abrr_list это вспомогательный список с образцами.
abrr_list = ['USA', 'UAE', 'GBR']

for name in raw_names:
    if name.upper() in abrr_list:
        normalized_names.append(name.upper())
    elif ' ' in name:
        name_list = name.split(' ')
        capitalize_name = []
        for item in name_list:
            capitalize_name.append(item.capitalize())

        normalized_names.append(' '.join(capitalize_name))
    else:
        normalized_names.append(name.capitalize())

print(normalized_names)

# ------------------------------------------------------------
raw_data = [
    [' 192.168.0.1:8080', ' 10.0.0.5 :22', '172.16.0.3 : 443  '],
    ['  8.8.8.8:53', ' 1.1.1.1 :  80', '  192.168.1.10:  3306'],
    [' 127.0.0.1 :5000', '  10.10.10.10:  8081 ', ' 0.0.0.0:   1234 '],
]

ips_list = []

for list in raw_data:
    for el in list:
        new_el = el.replace(' ', '').split(':')
        ips_list.append(new_el[0])


print(ips_list)
