from random import randint
from time import sleep

sorteio = randint(0,10)
tentativas = 0
acerto = False
print('De 0 a 10')
sleep(2)
print('Tente adivinhar o numero que pensei!')
sleep(2)


while not acerto:
    num = int(input("Digite um numero de 0 a 10: "))
    tentativas += 1
    sleep(1.4)
    if num != sorteio:
        print('\033[031mErrou')
        sleep(0.9)
        print('Tente novamente!\033[m')
        sleep(0.9)
    if num > sorteio:
        print('Pensei em numero um pouco \033[32mmenor\033[m')
    elif num < sorteio:
        print('Pensei em numero um pouco \033[32mmaior\033[m')

    if num == sorteio:
        acerto = True

print(f'\033[34mPARABENS!\033[m Voce acertou com {tentativas} tentativas.')