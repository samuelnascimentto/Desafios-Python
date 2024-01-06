velc = int(input('Digite a velocidade que o seu carro estava: '))

mult = velc-80

mult1 = mult*7


if velc >80:
    print('Tome cuidado! Voce ultrapassou os 80km/h')
    print(f'Voce foi multado em: R${mult1} por estar {mult}km/h acima da media.')
else:
    print('Parabens! Voce estava na velocidade certa: ')