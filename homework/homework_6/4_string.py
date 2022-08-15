word = input("Введіть рядок не менше 15(ти) символів: ")

while len(word) < 15:
    word = input("ПОМИЛКА!\nВведіть рядок не менше 15(ти) символів: ")

print("a. -",word[2])
print("b. -",word[-2])
print("c. -",word[:5])
print("d. -",word[:-2:])
print("e. -",word[1::2])
print("f. -",word[::2])
print("g. -",word[::-1])
print("h. -",word[::-2])
print("i. -",len(word))