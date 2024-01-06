from random import randint

lista = randint(1,100), randint(1,100), randint(1,100), randint(1,100),randint(1,100) 

print(' ')
print(f'Numeros sorteados: {sorted(lista)}')
print(' ')

#print(f'O maior numero foi {sorted(lista)[4]} e o menor foi {sorted(lista)[0]}')

print(f'O maior numero foi {max(lista)} e o menor foi {min(lista)}')
