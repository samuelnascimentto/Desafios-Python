p1 = float(input('Primeiro Segmento: ')) 

p2 = float(input('Segundo Segmento: '))

p3 = float(input('Terceiro Segmento: '))

isosceles = p1 == p2 != p3 or p1 == p3 != p2 or p2 == p3 != p1

escaleno = p1 != p2 != p3 != p1

equilatero = p1 == p2 == p3

triangulo = p1 + p2 > p3 and p1 + p3 > p2 and p2 + p3 > p1

if triangulo == True and triangulo== isosceles:
    print('Os segmentos acima PODEM FORMAR um triângulo Isosceles')

elif triangulo==True and triangulo == escaleno:
    print('Os segmentos podem formar um triângulo Escaleno.')

elif triangulo==True and triangulo == equilatero:
    print('Os segmentos podem formar um triângulo Equilatero.')
    
else:
    print('NÃO PODEM FORMAR UM TRIÂNGULO')

