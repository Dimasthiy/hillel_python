n1 = int(input('Кількість учнів першого класу: '))
n2 = int(input('Кількість учнів другого класу: '))
n3 = int(input('Кількість учнів третього класу: '))

print(f'Для першого класу необхідно: {n1 // 2 + n1 % 2} парт')
print(f'Для другого класу необхідно: {n2 // 2 + n2 % 2} парт')
print(f'Для третього класу необхідно: {n3 // 2 + n3 % 2} парт')