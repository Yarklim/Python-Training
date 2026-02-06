user_input = "Hello"
word = "hello"
greeting = "hi therE!"
toReplace = "Hi Bob! Hi Mary!"

newGretting = greeting.capitalize()  # 'Hi there!'
newStr1 = user_input.lower()  # В нижний регистр
newStr2 = user_input.casefold()  # В нижний регистр (делает оптимизацию сравнения строк)
count = greeting.count("h")  # 2 - Количество вхождений подстроки 'h' в строку
replaced1 = toReplace.replace("Hi", "Goodbay")  # Заменит все вхождения 'Hi' в строке
replaced2 = toReplace.replace(
    "Hi", "Goodbay", count=1
)  # Заменит первое вхождение 'Hi' в строке


# Список методов есть в шпаргалке!
# ===================================================================
