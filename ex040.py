not1 = int(input('Digite o valor da primeira nota: '))

not2 = float(input('Digite o valor da segunda nota: '))

not3 = float(input('Digite o valor da terceira nota: '))

med = (not1 + not2 + not3) / 3


if not1 and not2 and not3 < 10 :
    print('As notas so podem ser de 0 a 10!')


elif med < 5:
    print('O aluno foi REPROVADO')
    print(f'A media foi: {med:.1f}')  

elif med <= 6.9:
    print('O aluno ficara em RECUPERACAO!')
    print(f'A media foi: {med:.1f}')  
else:
    print('O aluno foi APROVADO!')
    print(f'A media foi: {med:.1f}')  



 