from time import sleep

inicio = int(input('Digite o numero que comecara a contagem: '))

fim = int(input('Digite o numero que terminara a contagem: '))

salto = int(input('Digite o numero de salto que deseja: ')) 

for c in range(inicio ,fim, - salto):
    print(c)
    sleep(0.8)
print('\033[11;31mFELIZ ANO NOVO!\033[m')  