print('-='*13)
print('SEQUENCIA DE FIBONACCI')
print('-='*13)

n = int(input('Digite quantos termos devo fazer: '))
a = 0
b = 1
c = 0
d = 0

while d < n:
    print(f'{c} ', end='-> ')
    d += 1
    c = a + b
    if d > 1:
        a = b
        b = c
print('FIM!')
