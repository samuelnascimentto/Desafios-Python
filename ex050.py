s = 0

for laco in range(1, 7):
    num = int(input(f'Digite o numero {laco}: '))
    if num % 2 == 0:
        s += num
print(f'A soma dos numeros pares foi: {s}')