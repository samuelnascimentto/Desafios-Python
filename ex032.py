ano = int(input('Digite o ano para saber se ele e bissexto: '))

if ano % 4 == 0 and ano % 100 == 0 or ano % 400 == 0 :

    print (f'O ano {ano} e bissexto!')

else:

    print(f'O ano {ano} nao e bissexto!')



