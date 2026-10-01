# ================= Range (диапазон) =================

x = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(3):
    print(i, 'Hello')

# ---- от и до ----
for i in range(2, 5):
    print(i, 'Hello')

# ---- от и до с шагом ----
for i in range(1, 7, 2):
    print(i, 'Hello')
