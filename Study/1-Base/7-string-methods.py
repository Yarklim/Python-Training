user_input = "Hello"
word = "hello"
greeting = "hi therE!"

newGretting = greeting.capitalize()  # 'Hi there!'
newStr1 = user_input.lower()  # В нижний регистр
newStr2 = user_input.casefold()  # В нижний регистр (делает оптимизацию сравнения строк)
count = greeting.count("h")  # 2 - Количество вхождений подстроки 'h' в строку
