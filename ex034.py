sal = int(input('Digite o valor do seu salario: '))
 
sal15 = sal * 0.15

sal10 = sal * 0.10

if sal <= 1250: 
    print(f'O seu aumento sera de: {sal15}')
else:
    print(f'O seu aumento sera de: {sal10}')