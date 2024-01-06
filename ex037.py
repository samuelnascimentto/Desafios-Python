num = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão: 

[1] converter para \033[1;32mBINÁRIO\033[m 
[2] converter para \033[1;33mOCTAL\033[m
[3] converter para \033[1;34mHEXADECIMAL\033[m''')
opcao = int(input('Qual a sua opção? '))

if opcao == 1:

    print(f'{num} convertido para binário é igual a {bin(num)[2:]}')

elif opcao == 2:

    print(f'{num} convertido para octal é igual a {oct(num)[2:]}')

elif opcao == 3:
    print(f'{num} convertido para hexadecimal é igual a {hex(num)[2:]}')
    

else:
    print('Opção \033[1;31mINVÁLIDA\033[m. Tente novamente!')
