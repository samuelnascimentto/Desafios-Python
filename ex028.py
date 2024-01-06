import random

num = int(input('Digite um numero de 0 a 5: '))

num1 = [0,1,2,3,4,5]

sort = int(random.choice(num1))

if num == sort:
    print('Parabens!!! Voce venceu')

else:
    print(f'Voce perdeu! O numero sorteado foi: {sort}')

