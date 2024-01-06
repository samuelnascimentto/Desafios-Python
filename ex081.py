num = []
elem = dec = 0 

while True:
    num.append(int(input('Digite um numero: ')))
    elem += 1

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Digite [S/N] para continuar: ')).upper().strip()
    if opcao == 'N':
        break
    

num.sort(reverse=True)
print()

if 5 in num:
    print('O numero 5 esta na lista')
else:
    print('O numero 5 nao foi digitado!')
print()
print(f'Foram digitados {elem} numeros. ')
print()
print(f'A lista invertida ficara: {num} ')