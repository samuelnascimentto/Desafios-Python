num = float(input('Digite a distancia da sua viagem e km: '))

abai = num * 0.5

acim = num * 0.45

if num <= 200 :

    print(f'O Valor da sua viagem sera: R${abai:.4}')

else:

    print(f'O valor da sua viagem sera: R${acim:.4}')