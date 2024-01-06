nom = str(input('Digite o seu nome completo: '))

esp = nom.strip()

sepa = nom.split()


print(f'O seu nome completo em letras maiusculas ficara: {nom.upper()}')

print(f'O seu nome completo em letras minusculas ficara: {nom.lower()}')

print(f'O seu nome completo tem: {len(nom)} {nom.strip(esp)} letras')

#print(f'O seu primeiro nome tem: {len(sepa[(0)])} letras')


print(f'O seu primeiro nome tem: {nom.find(" ")} letras')
