from datetime import date
data = date.today().year
nasc = int(input('Digite a data de nascimento do atleta: '))

idade = data - nasc 

if idade < 9: 
    print(f'O atleta tem {idade} anos')
    print('A categoria sera MIRIM! ')

elif idade < 14:
    print(f'O atleta tem {idade} anos')
    print('A categoria sera INFANTIL! ')

elif idade < 19:
    print(f'O atleta tem {idade} anos')
    print('A categoria sera JUNIOR! ')
elif idade <= 20:
    print(f'O atleta tem {idade} anos')
    print('A categoria sera ADULTO! ')
else:
    print(f'O atleta tem {idade} anos')
    print('A categoria sera MASTER! ')
