n1 = int(input('Digite o valor do primeiro segmento: '))

n2 = int(input('Digite o valor do segundo segmento: '))

n3 = int(input('Digite o valor do terceiro segmento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print(f'Os segmentos podem formar um Triangulo')
else: 
    print(f'Os segmentos nao podem formar um Triangulo')

