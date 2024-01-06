numeros = ('zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis' , 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('Digite um numero de 1 a 20: '))
    while num> 20 or num <1:
        num = int(input('\033[31mTente Novamente!\033[m\nDigite um numero de 0 a 20: '))
    break
print(f'Voce digitou o numero {numeros[num]}')

while True:
    opcao= str(input('Quer continuar? Digite [S/N]: ')).strip().upper()
    if opcao == 'S':
        num = int(input('Digite um numero de 0 a 20: '))
        while num> 20 or num <0:
            num = int(input('\033[31mTente Novamente!\033[m\nDigite um numero de 0 a 20: '))
            print(f'Voce digitou o numero {numeros[num]}')
    else:
        print('\033[31mTente Novamente!\033[m')
        opcao= str(input('Quer continuar? Digite [S/N]: ')).strip().upper()
        break




