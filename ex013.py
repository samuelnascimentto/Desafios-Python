salario = float(input('Informe seu sálario: R$'))

salario_aumento = salario + (salario * 15 / 100)

print('Salário final: R${:.2f}'.format(salario_aumento))