user_input = "Hello"
word = "hello"
greeting = "hi therE!"
toReplace = "Hi Bob! Hi Mary!"

print(user_input[1])  # 'e'
print(user_input[-1])  # 'o'

len(word)  # 5

newGretting = greeting.capitalize()  # 'Hi there!'
newStr1 = user_input.lower()  # В нижний регистр
newStr2 = user_input.casefold()  # В нижний регистр (делает оптимизацию сравнения строк)
new_user_input = user_input.strip()  # Очищает пробелы в начале и в конце строки
print(greeting.startswith("hi"))  # true
print(toReplace.startswith("hi"))  # false
print(greeting.endswith("!"))  # true
print(toReplace.endswith("?"))  # false
count = greeting.count("h")  # 2 - Количество вхождений подстроки 'h' в строку
replaced1 = toReplace.replace("Hi", "Goodbay")  # Заменит все вхождения 'Hi' в строке
replaced2 = toReplace.replace(
    "Hi", "Goodbay", count=1
)  # Заменит первое вхождение 'Hi' в строке

# ====================================================
# Список методов есть в шпаргалке!
# ====================================================

# =============== Форматирование строк ===============
name = "Yar"
age = "54"
print(f"User name: {name} | User age: {age}")
