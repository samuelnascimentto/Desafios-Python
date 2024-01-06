escolha = totpessoas = toth = totmulabaixo18 = f = 0 
while True:
    print('')
    sexo = str(input('Digite o seu sexo [H/M]: ')).upper().strip()
    print('')
    if sexo == 'H':
        toth+= 1
    elif sexo == 'M':
        sexo = 'mulher'
    else:
        print('OPCAO INAVALIDA!')

    print('')
    idade = int(input('Digite a sua idade: '))
    print("")
    if idade > 18:
        totpessoas += 1
    elif sexo == 'mulher' and idade< 18:
        totmulabaixo18 += 1

    print('')
    print('Quer continuar? ')
    escolha = str(input('Digite (S) para sim e (N) para Nao: ')).upper().strip()
    print('')
    if escolha == 'S':
        f = f
    elif escolha == 'N':
        print("Acabou!")
        break
    else:
        print('OPCAO INAVALIDA!')

print(f'O total de pessoas acima de 18 foi: {totpessoas} \nO total de homens cadastrados foi: {toth} \nO total de mulheres abaixo de 18 foi: {totmulabaixo18}')
