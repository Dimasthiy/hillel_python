num_1 = int(input("Введіть перше число першого списку: "))
num_2 = int(input("Введіть друге число першого списку: "))
num_3 = int(input("Введіть третє число першого списку: "))
num_4 = int(input("Введіть перше число другого списку: "))
num_5 = int(input("Введіть друге число другого списку: "))
num_6 = int(input("Введіть третє число другого списку: "))

lst_1 = [num_1, num_2, num_3]
lst_2 = [num_4, num_5, num_6]

lst_3 = []

count_1 = 0

for i in lst_1:
    if i not in lst_3:
        count_1 = count_1 + 1
        lst_3.append(i)

for a in lst_2:
    if a not in lst_3:
        count_1 = count_1 + 1
        lst_3.append(a)

print("Унікальних чисел разом:",count_1)
print("Унікальні числа:",lst_3)