value = 75
part = 16

if value <= 0:
    print("Value cant be 0 or less than 0")
elif part < 0:
    print("Part cant be less than 0")
else:
    percent = part / value * 100
    print(round(percent, 2), "%")


age = 0

if age <= 0 or age >= 150:
    print("Такого возраста не существует")
elif age >= 28 and age <= 149:
    print("Взрослый")
elif age >= 18:
    print("Подросток")
else:
    print("Ребенок")

# ========= match =========
score = 85

match score:
    case s if s >= 90:
        print("Оценка отлично")
    case s if s >= 75:
        print("Оценка хорошо")
    case s if s >= 60:
        print("Оценка удовлетворительно")
    case _:
        print("Тест не сдан")
