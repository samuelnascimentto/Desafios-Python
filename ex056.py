nomevelho = 0
menores = 0
mulher= 0
media = 0

ate= int(input('Digite o numero de pessoas: '))

for laco in range(1,ate+1):   
    nome = str(input(f'Digite o {laco}a nome: ')).upper()

    print(f'Ola {nome}!')
    idade = int(input('Digite a sua idade: '))

    sexo = str(input('Agora o seu sexo [M/F]: ')).upper()
    print('-'*26 )
    
    media += idade

    if sexo == 'F' :
        mulher += 1
        if idade < 21:
            menores += 1
        
    elif sexo == 'M':
        if laco == 1:
            idade = nomevelho
        if idade > nomevelho:
            nomevelho = idade

print(f'A idade media do grupo e: {media/ate:.1f}')
print(f'O homem mais velho tem: {nomevelho} anos')
print(f'ha {mulher} mulheres, e {menores} abaixo de 21 anos ')

