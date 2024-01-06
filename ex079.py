num = []


while True:
    val = int(input('Digite um numero: '))
    if val in num:
        print('Este numero ja esta na lista!')
    else:
        num.append(val)

    opcao = str(input('Quer continuar? Digite [S/N]: ')).upper().strip()
    if opcao == 'N':
        break
        





print(f'Voce digitou os numeros: {sorted(num)}')