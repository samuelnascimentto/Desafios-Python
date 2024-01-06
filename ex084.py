temp = [] 
princ = []
numcad = maior = menor = p = 0
while True:

    temp.append(str(input('Digite o seu nome: ')))
    temp.append(float(input('Digite a seu peso: ')))
    princ.append(temp[:]) 
    princ.clear()

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Digite [S/N] para continuar: ')).upper().strip() 
    if opcao == 'N':
        break

print()
print(f'O total de pessoas cadastradas foi de: {len(princ)}')
print(f'O maior peso foi de: {}')