a = int(input("Введіть число: "))
b = list()
n = 0

while a > n:
    n = n + 1
    p = n ** (0.5)
    s = int(p)
    len_p = len(str(p))
    if len_p <= 3:
        r = s ** 2
        b.append(r)

print(a, ":", b)