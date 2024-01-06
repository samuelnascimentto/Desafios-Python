import math

angs = float(input('Digite o angulo que voce quer: '))

sen = math.sin(math.radians(angs))

print(f'O angulo de {angs} tem o Seno de: {sen:,.2f}')

coss = math.cos(math.radians(angs))
print(f'O angulo de {angs} tem o Cosseno de: {coss:,.2f}')

tang = math.tan(math.radians(angs))
print(f'O angulo de {angs} tem a Tangente de: {tang:,.2f}')