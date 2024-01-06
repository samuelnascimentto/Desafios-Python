soma = totnum = med = 0

c = 0
while c == 0:
    num = int(input('Digite um valor [Aperte 999 para eu parar!] : '))
    if num == 999:
        break
    totnum += 1
    soma += num
    med = soma / totnum
print(f'O total de numeros digitados foi: {totnum} \nA soma dos numeros foi: {soma} \nA media dos numeros foi {med:.1f}')