expressao = str(input('Digite a expressao com parenteses: '))
parentesesabertos = list()
parentesesfechados = list()

for c in expressao:
    if c == '(':
        parentesesabertos.append(c)
    elif c == ')':
        parentesesfechados.append(c)

if len(parentesesabertos) == len(parentesesfechados):
    print(f'A expressao esta correta! Voce abriu e fechou {len(parentesesabertos)} parenteses.')
else:
    print(f'A expressao esta incorreta! Voce abriu {len(parentesesabertos)} parenteses, '
          f'porem fechou {len(parentesesfechados)}.')