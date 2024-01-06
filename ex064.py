from time import sleep

n = int(input('Digite um numero: '))
print('So vou parar quando digitar o numero: 0')
sleep(2)
soma = 0
tot = 0
laco = 0

while n != laco:
    n = int(input('Digite um numero: '))
    tot += 1
    soma += n

print(f'Terminei! A soma de todos os numeros foi {soma} e voce digitou {tot} numeros.')

