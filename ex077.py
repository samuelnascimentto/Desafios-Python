palavras = tuple(str(input(f'Digite a {c}ª palavra: '))
                 
for c in range(1, 6))
print('=' * 40,end='')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogáis: ',end='')
    for vogal in palavra:
        if vogal.lower() in 'aeiou':
            print(f'{vogal.lower()}',end=' ')
print(' ')
print('=' * 40)