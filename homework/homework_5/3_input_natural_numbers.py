a = list()
b = int(input("Введіть число: "))

while b != 0:
    a.append (b)
    print(a)
    b = int(input("Введіть число: "))

sum_a = sum(a)
average_a = sum_a/len(a)
min_a = min(a)
max_a = max(a)
amount_p_a = sum(1 for i in a if i % 2 == 0)
amount_np_a = sum(1 for i in a if i % 2 != 0)

print("Сума чисел:",sum_a)
print("Середнє арифметичне чисел:",average_a)
print("Мінімальне введене число:",min_a)
print("Максимальне введене число:",max_a)
print("Кількість парних чисел",amount_p_a)
print("Кількість непарних чисел",amount_np_a)