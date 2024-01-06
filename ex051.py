num = int(input('Digite o primeiro termo: '))

r = int(input('Digite a razao do termo: '))

ate = int(input('Digite ate aonde quer que eu faca: '))

for laco in range(num, ate+1, r):
    print(laco, end=' -> ')