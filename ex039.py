nasc = int(input('Digite o ano em que nasceu: '))

anos = 2023 - nasc

faltam = 18 - anos 


print(f'Quem nasceu em {nasc} tem {anos} anos')

if anos > 18: 
    passou = anos - 18
    print(f'Voce passou {passou} anos da idade de alistamento!')
    anopassou =  nasc + 18
    print(f'O ano que voce deveria alistar-se foi: {anopassou}')
    
elif anos < 18:
    data_alis = nasc+ 18
    print(f'Voce nao possui idade para se alistar!') 
    print(f'Faltam {faltam} anos para o seu alistamento!')
    print(f'O ano do seu alistamento sera no ano {data_alis}')
else:
    print('Esta na hora de alistar-se!')