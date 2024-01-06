gasto = totprod = opcao = menor = cont = 0
barato = ''
while True:
    print('_'*30)
    preco = float(input('Digite o valor do produto R$: '))
    gasto += preco
    if preco > 1000:
        totprod += 1
    cont  += 1

    print('_'*30)
    nome = str(input('Digite o nome do produto: ')).upper().strip()
    opcao= ' '
    if cont == 1 or preco < menor :
        menor = preco
        barato = nome

    while opcao not in 'SN':
        opcao = input('Quer continuar? {S/N}').upper().strip()
    if opcao == 'N':
        break
print(f'O total gasto foi R$: {gasto} \nO total de produto acima de R$:1000 foi: {totprod} \nO preco do produto mais barato foi R$: {menor} e o seu nome e: {barato}')
