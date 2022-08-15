word = str(input("Введіть 2 слова через пробіл: "))
space_check = word.count(" ")

while space_check != 1:
    word = str(input("Невірний формат вводу!\nВведіть 2 слова через пробіл: "))
    space_check = word.count(" ")
    if space_check == 1:
        break

space_num = word.find(" ")
word_a = word[:space_num]
word_b = word[space_num+1:]

word_a_inv = word_a[::-1]
word_b_inv = word_b[::-1]
word_a_inv_t = word_a_inv.title()
word_b_inv_t = word_b_inv.title()

print(word_a_inv_t,word_b_inv_t)