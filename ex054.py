from datetime import date

menor = 0

maior = 0

for laco in range(1,8):
    nasc = int(input('Digite o seu ano de nascimento: '))
    idade = date.today().year - nasc
    if idade <= 21:
        menor += 1
        
    elif idade >= 18:
        maior +=  1

print(f'Existem {menor} menores de idade e {maior} maiores de idade ')
