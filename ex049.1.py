num1 = (int(input('Digite um numero! Irei fazer a sua tabuada: ')))

num2 = (int(input('Digite ate qual numero quer quer eu faca a tabuada: ')))

cont = 0

for laco in range(1, num2, ):
    cont += 1

print(f'{num1} x {cont} =  {num1*cont}')
