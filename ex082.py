num = []
list0 = []
n =0
list1 = []

while True:
    n = int(input('Digite um numero: '))
    num.append(n)
    opcao = ' '

    if n %2 ==0:
        list0.append(n)
    else:
        list1.append(n)

    while opcao not in 'SN':
        opcao = str(input('Digite [S/N] para continuar: ')).upper().strip() 
    if opcao == 'N':
        break



print(f'Os numeros digitados foram: {num}  \nOs numeros pares sao: {list0}  \nOs numeros impares sao: {list1}')
