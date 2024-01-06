dia = int(input('Dias alugado: '))
km = int(input('Km rodados: '))

valor = (dia * 60) + (km * 0.15)

print('Total a pagar: R${:.2f}'.format(valor))