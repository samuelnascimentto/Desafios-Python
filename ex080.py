import bisect
numbers = []
for i in range(5):
    n = int(input('Digite um numero: '))
    bisect.insort(numbers, n)
    print(f'Numero {n} na posicao {numbers.index(n)}')
print(f'Os valores digitados foram {numbers}')