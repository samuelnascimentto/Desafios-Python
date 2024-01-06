num = int(input('Digite um numero: '))

if num == (1,2,3,5,7,11):
    print('Ele e numero primo')
elif num % 2 == 0 or num % 3 == 0 or num % 5 ==0 or num % 11 ==0:
    print('Ele nao e numero primo')
else:
    print('Ele e numero primo')
