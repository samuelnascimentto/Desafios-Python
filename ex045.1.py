from random import choice
from time import sleep
print(''' Voce quer jogar JOKENPO?
Digite
[ 0 ] \033[11;34mSe voce quiser\033[m      
[ 1 ] \033[11;31mCaso nao queira\033[m      
      ''')

opcao = int(input('Digite 0 ou 1: '))

if opcao == 0:
    print('-='* 11)
    print('''    
    [ 0 ] PEDRA   
    [ 1 ] PAPEL     
    [ 2 ] TESOURA     
          ''')  
    print('-='* 11)  
    jogador = int(input('Escolha outro numero: '))

    print('\033[11;30mJO\033[m')
    sleep(0.8)
    print('\033[11;30mKEN\033[m')
    sleep(0.8)
    print('\033[11;30mPO!\033[m')
    sleep(0.8)
    if jogador == 0:
        print('Voce escolheu PEDRA!')
    
    elif jogador == 1:
        print('Voce escolhheu PAPEL!')

    elif jogador == 2:
        print('Voce esolheu TESOURA!')

    else:
        print('\033[11;31mOPCAO INVALIDA!\033[m')

    list = (0,1,2)
    computador = choice(list)  
    if computador == 0: 
        print('O PC escolheu PEDRA!')

    elif computador == 1:
        print('O PC escolheu PAPEL!')
    
    elif computador == 2:
        print('O PC escolheu TESOURA!')

    if jogador == computador:
        print('\033[11;33mEMPATOU!\033[m')

    elif (jogador == 0 and computador == 1) or(jogador == 1 and computador == 2) or (jogador == 2 and computador == 0):
        print('Voce \033[11;31mPERDEU!\033[m')

    else:
        print('Voce \033[11;34mGANHOU!\033[m')
    
elif opcao == 1:
    print('Esta bom! Seu chato! Nao iremos jogar!' )

else:
    print('\033[11;31mOPCAO INVALIDA!\033[31m')
