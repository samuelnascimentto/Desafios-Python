import random

a1 = input('Nome do 1° aluno: ')

a2 = input('Nome do 2° aluno: ')

a3 = input('Nome do 3° aluno: ')

a4 = input('Nome do 4° aluno: ')

alunos = a1,a2,a3,a4

sort = random.sample(alunos, 4)

print(f'O nome dos quatro alunos sorteados foram: {a1}, {a2}, {a3} e {a4}.')


print(f'A ordem do sorteio da sala foi: {sort}')