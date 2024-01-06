casa_val = int(input('Digite o valor da casa R$ '))

sala_val = int(input('Digite o valor do salario R$ ')) 

anos = int(input('Digite os anos de fincanciamento: '))

sal30= sala_val* 0.30

meses = anos * 12

pag_mes = casa_val / meses 

if pag_mes <= sal30:
    print('Parabens!')
    print('Voce conseguiu a aprovacao:')
    print(f'A mensalidade sera: R$: {pag_mes:.0f} por mes')
else:
    print('Sinto muito!')
    print ('voce nao tem orcamento para financiar essa casa')
    print(f'Voce tem que pagar R$: {pag_mes:.0f} por mes, mas seu salario mensal e R$: {sala_val} ')