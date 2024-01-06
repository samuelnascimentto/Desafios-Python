sexo = str(input('Digite [M/F] para o seu sexo: ')).upper().strip()   

if sexo == 'M':
   print(f'O seu sexo e masculino')
   
elif sexo == 'F':
    print(f'O seu sexo e feminino')

elif sexo == 'MASCULINO':
    print(f'O seu sexo e masculino')

elif sexo == 'FEMININO':
    print(f'O seu sexo e feminino')

while sexo not in 'M,F':
    sexo = str(input('Dado invalido! Informe seu sexo: [M/F] ')).upper().strip()

    if sexo == 'M':
        print(f'O seu sexo e masculino')
        
    elif sexo == 'MASCULINO':
        print(f'O seu sexo e masculino')

    elif sexo == 'FEMININO':
        print(f'O seu sexo e feminino')

    elif sexo == 'F':
        print(f'O seu sexo e feminino')
