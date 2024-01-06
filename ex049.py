num  = int (input('Digite um numero para que eu faca a tabuada: '))

ate = int(input('Digite ate quando quer que eu faca: '))

for laco in range(1, ate+1):
    print(f'{num}  x  {laco}  = {num*laco}')
