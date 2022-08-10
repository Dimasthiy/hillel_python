a = int(input("Введіть число: "))

while a > 9:
    b = a // 10
    c = a % 10
    a //= 10
    while b != 0:
        if c == b % 10:
            print('Так')
            exit(0)
        b //= 10
print('Ні')