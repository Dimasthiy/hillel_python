word = input("Введіть число від 3 до 9: ")
n = 1

if word.isdigit():
    num = int(word)
else:
    print("Невірний формат вводу!")
    exit()
if num < 3 or num > 9:
    print("Невірний формат вводу!")
    exit()

for i in range(num + 1):
    for j in range(1, i + 1):
        print(j, end='')
    for h in range(1, i)[::-1]:
        print(h, end='')
    print()


