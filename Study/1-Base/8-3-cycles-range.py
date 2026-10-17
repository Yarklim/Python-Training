from data.currencies import currencies

# ================= Range (диапазон) =================

x_list = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x_tuple = tuple(range(10))  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
y = list(range(2, 21, 2))  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
z = list(range(20, 1, -2))  # [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]

y_item_index = y.index(6)  # 2
# ----------------------------------------------------
for i in range(len(currencies) - 1):
    if currencies[i][0] == 'PHP':
        currencies.pop(i)

print(currencies)

# # ---- от и до ----
# for i in range(2, 9):
#     print(i)

# # ---- от и до с шагом ----
# for i in range(1, 7, 2):
#     print(i)

# # -------------------------
# for _ in range(3):
#     print('Hello')
