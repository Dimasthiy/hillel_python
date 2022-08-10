a = int(input("Введіть число: "))
n = 0
while a > n:
    n = n + 1
    p = n * n
    len_n = len(str(n))
    if len_n == 1.0:
        r = p % 10
        if r == n:
            print(n, "*", n, "=", p)
    elif len_n == 2.0:
        r = p % 100
        if r == n:
            print(n, "*", n, "=", p)
    elif len_n == 3.0:
        r = p % 1000
        if r == n:
            print(n, "*", n, "=", p)
    elif len_n == 4.0:
        r = p % 10000
        if r == n:
            print(n, "*", n, "=", p)
    elif len_n == 5.0:
        r = p % 100000
        if r == n:
            print(n, "*", n, "=", p)
    elif len_n == 6.0:
        r = p % 1000000
        if r == n:
            print(n, "*", n, "=", p)