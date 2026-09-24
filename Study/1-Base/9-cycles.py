# =============== FOR ===============
# for i in range(3):
#     print(i, 'Hello')

# # ---- от и до ----
# for i in range(2, 5):
#     print(i, 'Hello')

# # ---- от и до с шагом ----
# for i in range(1, 7, 2):
#     print(i, 'Hello')

# ============== WHILE ==============
user_input = input('Enter something:\n')

vowels = 'eyuioa'
vowels_count = 0
no_t_char = False
index = 0

while index < len(user_input):
    char = user_input[index]
    index += 1

    if char in vowels:
        if char == 'a':
            continue
        vowels_count += 1

    elif char == 't':
        break

else:
    no_t_char = True

print(vowels_count)
print(no_t_char)
