val = int(input('Digite o valor do produto: '))

print('Digite um numero de 1 a 4')
print('''[ 1 ] Dinheiro ou cheque
[ 2 ] a vista no cartao
[ 3 ] 2x no cartao 
[ 4 ] 3x ou mais no cartao ''')

pagam = int(input('Escolha a forma de pagamento: ')) 

if pagam < 1:
    print ('OPCAO INVALIDA')

elif pagam > 6:
    print ('OPCAO INVALIDA')

elif pagam == 1: 
    print(f'O valor ficara R$:{val - (val * 0.10)}')
    
elif pagam == 2:
    print(f'O valor ficara R$:{val - (val * 0.05)}')

elif pagam == 3:
    parce = val / 2
    print(f'As parcelas seram de: {parce}')
    print(f'O valor ficara R$:{val}')

else:
    numpar = int(input('Digite o numero de parcelas: '))

    print(f'Ficara R$:{val / numpar:.2f} por parcelas')
    print(f'O valor ficara R$:{val + (val * 0.20):.2f}')

