num_1 = int(input("Введіть перше число: "))
num_2 = int(input("Введіть друге число: "))
num_3 = int(input("Введіть третє число: "))
num_4 = int(input("Введіть четверте число: "))
num_5 = int(input("Введіть п`яте число: "))

lst = [num_1, num_2, num_3, num_4, num_5]
print(lst)

k = int(input("Введіть число для індексу k: "))

lst.pop(k)
print(lst)