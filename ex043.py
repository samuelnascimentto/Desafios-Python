peso = float(input('Digite o peso da pessoa: '))

altura = float(input('Digite a altura da pessoa: '))

imc = peso / (altura**2)

if imc <= 18.5:
    print(f'O seu imc e: {imc:.1f}')
    print(f'Abaixo do peso!')
    
elif imc <= 25:
    print(f'O seu imc e: {imc:.1f}')
    print('PESO IDEAL!')

elif imc <= 30 :
    print(f'O seu imc e: {imc:.1f}')
    print('Obesidade grau I!')

elif imc <= 40:
    print(f'O seu imc e: {imc:.1f}')
    print('Obesidade garu II!')

else:
    print(f'O seu imc e: {imc:.1f}')
    print('Obesidade grau III !')



