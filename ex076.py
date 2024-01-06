ti = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.0, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120, 'Canetas', 22.20)
print('-'*30)
print('{:^30}'.format('LISTAGGEM DE PREÇOS'))
print('-'*30)
for c in range(0, len(ti)):
    if c % 2 == 0:
        print(f'{ti[c]:.<20} R${ti[c+1]}')
print('-'*30)