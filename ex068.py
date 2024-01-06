from random import randint
soma = jogo = parimpar = resultado = 0
v = 1

while True:
    computador = randint(0,10)
    jogador = int(input('Digite um valor: '))
    escolha = str(input('Escolhe Par ou Impar? [P/I]: ')).upper().strip()
    print(' ')

    if escolha == 'I':
        escolha = 'Impar'
    else:
        escolha = 'Par'

    soma = computador+ jogador
    parimpar = soma %2
    if parimpar == 1:
        jogo = 'Impar'
    elif parimpar == 0:
        jogo = 'Par'

    if jogo == escolha:
        resultado = print('\033[34mVoce ganhou!\033[m')
        print(f'O computador escolheu {computador} e voce {jogador}.\nA soma de {computador} +{jogador} = {soma} que e um numero: {jogo}')
        print(' ')
        v += 1

    elif jogo != escolha: 
        resultado = print('\033[31mVoce perdeu!\033[m')
        print(f'O computador escolheu {computador} e voce {jogador}.\nA soma de {computador} + {jogador} = {soma} que e um numero: {jogo}')
        print('Acabou!!! ')
        print(' ')
        break

if v == 1: 
    print(f'Voce ganhou {v} vez') 
else:
    print(f'Voce ganhou {v} vezes' )
