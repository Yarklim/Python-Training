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
# ----------------------------
palindrome = 'racecar'

i = 0
j = len(palindrome) - 1

is_palindrome = True

while i < j:
    if palindrome[i] != palindrome[j]:
        is_palindrome = False
        break

    i += 1
    j -= 1

# print(is_palindrome)
# ----------------------------
el = ''
count = 10
i = 1

while i <= count:
    spaces = ' ' * (count - i)
    stars = ' '.join('*' * i)

    el += spaces + stars + '\n'

    i += 1

print(el)
