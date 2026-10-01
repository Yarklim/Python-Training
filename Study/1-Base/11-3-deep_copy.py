# ==================== Сравнение list and tuple ===================
x = (1, 2, 5, 10, -50, -50, 148)
y = list(x)
z = [1, 2, 5, 10, -50, -50, 148]
i = [1, 2, 5, 10, -50, -50, 14]
j = [10, 2]

print(x == y)  # False
print(z == y)  # True
print(z is y)  # False
print(i > z)  # False
print(j > z)  # True

# =================== Поверхностная копия =====================
import copy

list_x = [[1, 2, 5], [10, -50], -50, 148]
list_y = list(list_x)  # или list_x[:]

list_i = copy.deepcopy(list_x)  # полная глубокая копия

list_x[0].clear()
list_x.remove(148)

print(list_x)  # [[], [10, -50], -50]
print(list_y)  # [[], [10, -50], -50, 148]
print(list_i)  # [[1, 2, 5], [10, -50], -50, 148]
