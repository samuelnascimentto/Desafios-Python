n = int(input('Digite um numero para saber o fatorial: '))
f = 1
for i in range(1, n + 1):
    f *= i
print(f'O resultado de {n}! e {f}')
