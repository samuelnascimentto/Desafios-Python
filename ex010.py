real = float(input('Informe seu dinheiro: R$ '))

dolar = 3.96
euro = 4.27
conversao_dolar = real / dolar
conversao_euro = real / euro

print(f'Com R$ {real:.2f} você pode comprar $ {conversao_dolar:.2f}')
print(f'Com R$ {real:.2f} você pode comprar £ {conversao_euro:.2f}')