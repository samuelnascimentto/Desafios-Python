maior = 0
menor = 0

for laco in range(1 , 4):
    peso = float(input(f'Digite o {laco} peso: '))
    if laco == 1:
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso

print(f'O menor peso e: {menor}')
print(f'O maior peso e: {maior}')