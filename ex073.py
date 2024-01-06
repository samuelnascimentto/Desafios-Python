print('-'*30)
print('BRASILEIRAO INICIO DE 2023')
print('-'*30)

tabela = ('BOTAFOGO', 'FLAMENGO', 'GRÊMIO', 'SÃO PAULO',
         'FLUMINENSE', 'PALMEIRAS', 'Bragantino', 'Athletico-PR',
         'Fortaleza', 'Cruzeiro', 'Internacional', 'Atlético-MG', 
         'Cuiaba', 'Santos', 'Corinthians', 'Bahia', 'Goías',
         'Coritiba', 'Vasco', 'America - MG')

for t in tabela :
    print(t)
print(' ')
print('Escolha uma das opções a baixo: \n'
      '[1] Para ver os Tres primeiros colocados \n'
      '[2] Para ver os Tres Ultimos colocados \n'
      '[3] Em ordem Alfabetica. \n'
      '[4] Buscar a classificacao do santos \n'
      '[5] Para encerrar')
while True:
    opcao = int(input('Qual você escolhe: '))
    if opcao == 1:
     print(tabela[:3])
    elif opcao == 2:
        print(tabela[7:])
    elif opcao == 3:
        print(sorted(tabela))
    elif opcao == 4:
        print(f'A posicao do Santos na tabela e: {tabela.index("Santos")+1}a ') 
    else:
        break
print('Obrigado!')