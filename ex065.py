cont = 1
num = int(input('Digite um número? '))
user = str(input('Quer continuar? {S/N} ')).strip().lower()
soma = maior = menor = num
while user != 'n':
    num = int(input('Digite um número? '))
    user = str(input('Quer continuar? {S/N} ')).strip().lower()
    soma += num
    if num > maior:
        maior = num
    if num < menor: 
        menor= num
    cont += 1
print(f'Você digitou {cont} números e a média foi {soma:.2f} \nO maior valor foi {maior} e o menor foi {menor}')

