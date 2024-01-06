frase = str(input("Digite uma frase! ")).strip().lower()
frase = frase.replace(" ", "")
inverso = ""

for c in range(len(frase)-1, -1, -1):
    inverso += frase[c]

if frase == inverso:
    print("A Frase e um palindromo!")
else:
    print("A Frase nao e um palindromo! ")