c = 0
while True:
    tabuada = int(input('Digite um numero que farei a sua tabuada: '))
    if tabuada <0:
        break
    while c < 10: 
        c +=1
        print(f'{tabuada} x {c} = {tabuada*c}')
    c = 0

print('Programa encerrado!')
