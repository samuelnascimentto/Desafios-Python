n = int(1)
n1 = int(11)
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da P.A.: '))

while n < n1:
    an = a1 + (n - 1 )* r
    print (an, end= ', ')
    n += 1  

print(f'Programa encerrado, com {n} termos mostrados')

