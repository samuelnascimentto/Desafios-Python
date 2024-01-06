n1 = int(input('Digite o primieiro numero: '))

n2 = int(input('Digite o segundo numero: '))

n3 = int(input('Digite o terceiro numero: '))

if n1 == n2 == n3:
    
    print('Os números digitados são iguais.')

else:

    maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3

    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O maior numero que voce digitou foi : {maior} e o menor foi: {menor}')

