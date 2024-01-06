par = 0
num = (int(input('Digite o primeiro numero: ')),
        int(input('Digite o segundo numero: ')),
        int(input('Digite o terceiro numero: ')),
        int(input('Digite o quarto numero: ')),
        int(input('Digite o quinto numero: ')))
print(sorted(num))

print(f'O numero 9 foi digitado {num.count(9)} vezes e o numero par {par}')
print(f'O numero 3 apareceu na {num.index(3)+1} posicao ')

print('Os valores pares digitados são: ', end=' ')
for n in num:
    if n % 2 ==0:
        print(n, end=' ')
