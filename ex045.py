import random

print('Vamos jogar jokenpo? ')
  

print ('Escolha um numero') 
print('''
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA 
      ''')
    
jok = int(input('Digite um numero: '))

if jok == 1:
    print('Voce escolheu PEDRA')

elif jok == 2:
    print('Voce escolheu PAPEL')

elif jok == 3:
    print('Voce escolheu TESOURA')

list = (1,2,3)

sort = random.choice(list) 
    
if sort == 1:
    print('Eu escolhi PEDRA')

elif sort == 2:
    print('Eu escolhi PAPEL')

elif sort == 3:
    print('Eu escolhi TESOURA')



if sort == jok:
    print('EMPATOU')

elif (jok == 1 and sort == 2) or (jok == 2 and sort == 3) or (jok == 3 and sort == 1):
    print ("VOCÊ PERDEU!")

else:
    print('PARABENS!')
    print('VOCE GANHOU!')






