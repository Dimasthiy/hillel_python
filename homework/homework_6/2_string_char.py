word = input("Введіть слово: ")
num = list()
n = ""
for i in word:
    if i.isdigit():
        n = n + i
    else:
        if n != "":
            num.append(int(n))
            n = ""
if n != "":
    num.append(int(n))

print(num)