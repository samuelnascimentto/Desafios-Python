posicaomen = posicaomai = 0

num = []

for c in range(0,5):
    num.append(int(input(f'Digite o valor na posicao {c} : ')))    

print('')
print(f'Voce digitou os valores: {(num)}')
print('')
print(f'O menor numero digitado foi: {min(num)} \nO maior numero digitado foi: {max(num)}')
print()

for c, v in enumerate(num):
    if v == min(num):
        print(f'o menor valor está na posição {c}')
        print('')
    if v == max(num):
        print(f'o maior valor está na posição {c}')