print('Escolha o sabor da pizza:')

print('''[ 1 ] Calabresa 
[ 2 ] Mussarela 
[ 3 ] Portuguesa
[ 3 ] Marguerita 
[ 4 ] Frango com catupiry     
[ 5 ] Bauru     
[ 6 ] 4 queijo           ''')

pizza = int(input('Escolha um numero: '))

if pizza < 1:
    print('OPCAO INVALIDA!')

elif pizza > 6: 
    print('OPCAO INVALIDA!')

elif pizza == 1:
    print(f'A sua pizza de CALABRESA logo ficara pronta! ')

elif pizza == 2:
   print(f'A sua pizza de MUSSARELA logo ficara pronta! ')

elif pizza == 3:
    print(f'A sua pizza de MARGUERITA logo ficara pronta! ')

elif pizza == 4:
    print(f'A sua pizza de FRANGO COM CATUPIRY logo ficara pronta! ')

elif pizza == 5:
    print(f'A sua pizza de BAURU logo ficara pronta! ')

else:
    print(f'A sua pizza de 4 QUEIJO logo ficara pronta! ')