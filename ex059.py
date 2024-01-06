sim = False
while not sim:
    num1 = int(input('Digite o 1a valor: '))

    num2 = int(input('Digite o 2a valor: '))
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior (Para saber qual e o maior)
    [ 4 ] Para digitar novamente
    [ 5 ] Finalizar
    ''')
    opcao = int(input('\033[33mDigite o numero aqui: \033[m'))
    if opcao == 1:
        soma = num1+ num2
        print(f'A soma de {num1} e {num2} sera: {soma}')

    elif opcao == 2:
        multi = num1 * num2
        print(f'A multiplicacao de {num1} e {num2} sera: {multi}')


    elif opcao == 3:
        if num1 >num2:
            print(f'O maior numero entre {num1} e {num2} e: {num1}')
        else:
            print(f'O maior numero entre {num1} e {num2} e: {num2}')

    elif opcao == 4:
        sim = False

    elif opcao == 5:
        sim = True
    else:
        print('\033[31mOPCAO INVALIDA!\033[m')
        sim = True
print('\033[30mOBRIGADO\033[m! Por ter usado o nosso MENU.')
