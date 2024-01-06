fras = str(input('Digite uma frase qualquer: ')) .upper() .strip()

letra = str(input('Digite a letra que voce quer solucionar: ')) .upper() .strip()

fras0 = fras.count("A") 
 
fras1 = fras.find("A")+1

fras2 = fras.rfind("A")+1


print(f' A letra {letra} aparece: {fras0} vezes ')

print(f'A primeira letra {letra} aparece em: {fras1} ')

print(f'A ultima vez em que aparece a letra {letra} e na {fras2} caractere')
