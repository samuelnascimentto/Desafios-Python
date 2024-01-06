preco = float(input('Informe o preço do produto: R$'))

total = preco - (preco * 5 / 100)

print('Total à pagar com 5% de desconto: R${:.2f}'.format(total))