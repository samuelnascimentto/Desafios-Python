largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))

area = largura * altura
quantidade_tinta = area / 2

print('A parede tem uma área de {}m².'.format(area))
print('Será necessário {}L de tinta para pintar a parede.'.format(quantidade_tinta))