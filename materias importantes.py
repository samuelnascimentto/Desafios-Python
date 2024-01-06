#Bom eu apenas irei resumir aquilo que foi passado no curso.

#isalpha serve para ver se o string recebido tem uma letra alfabetica

#ispace serve para ver se o string recebido tem um caractere com espaco

#isalnum serve para ver se o string recebido tem um caractere com numerica

#isupper serve para ver se o string recebido tem um caractere com letra maiuscula

#islower serve para ver se o string recebido tem um caractere com letra minuscula

#istitle serve para ver se o string recebido tem um caractere com a primeira maiuscula

#tem tambem os imports e os principais q utilizei foram: math, mas existem outros tbm


#AULA 09 

frase = ('Curso em Video Python')

#len(frase) vai contar quantos caracteres tem a string

#frase.count('o') ele vai buscar na string todos os 'o' q tem na string. Porem pode ser usado para procurar nome completos ou cidades (pode acrescentar mais de uma coisa na pesquisa basta colocar a ',' virgula para separar o que se quer pesquisar.)

# frase.find('deo') find significa encontrar. Ou seja ele vai te mostrar em que numero de caractere ele encontrou o deo que seria no carcatere 11.

#'curso' in frase. O string "in" significa existe 'curso' dentro da string frase? ou qualquer outra coisa que deseja pesquisar usa o in 

#frase.replace ('Python','Android'): replace signicfica troca. Ou seja trocar a a palavra Pyhon por Android. (Nao esqueca que no python a palavra maiuscula se torna outra palavra)

#frase.upper() colocara tudo que estiver em minusculos vai para o maiusculo                        O seu inverso e o .lower

#frase.capitalize(): coloca todas as primeiras letras das palavras em maiusculas. Que no caso seriam: C,E,V,P

#frase.strip(): Eliminara todos os espacos desnecessarios tanto os do inicio como os do final.

#frase.rstrip(): (r de right) elimina todos os espacos da direita, consequentemente existe a lstrip, com a mesma funcao mas essa comeca pela left(esquerda).

h = ('funcionalidades de divisao: ')

#frase.split(): Ele ira dividir uma lista de todas palavras do caractere

#'-'.join(frase): Join significa juntar. Ele ira juntar cada palavra da lista junto com o '-' entao ficara         (Curso-em-Video-Python) 

                                # AULA 11 
 #  CORES EM PYHTON 

# ============<={=P=A=D=R=Ã=O===D=E===C=O=R=E=S===A=N=S=I=}=>==============

# ->Comando Geral: Dentro de uma str, \033[style;text;backm

#    STYLES                          |                TEXTS                         |BACKS
#                                    |                                              |
# 0 => none                          |   30 => preto                                |40 => as mesmas cores
# 1 => negrito                       |   31 => vermelho                             |41 ...
# 4 => sublinhado                    |   32 => verde                                |42
# 7 => negativo                      |   33 => amarelo                              |43
#                                    |   34 => azul                                 |44
#                                    |   35 => roxo                                 |45
#                                    |   36 => ciano                                |46
#                                    |   37 => cinza claro                          |47
#                                    |   90 => cinza escuro                         |100
#                                    |   91 => vermelho claro                       |101
#                                    |   92 => verde claro                          |102
#                                    |   93 => amarelo claro                        |103
#                                    |   94 => azul claro                           |104
#                                    |   95 => magenta claro                        |105
#                                    |   96 => ciano claro                          |106
#                                    |   97 => branco                               |107

# PARA ANULAR A COR E SO DIGITAR \033[m no final do print

print('VEJA SO: \033[11;30mEXEMPLO\033[m')

print('PARA A COR \033[;30m CINZA!\033[m') 
print('PARA A COR \033[;31m VERMELHO!\033[m')
print('PARA A COR \033[;32m VERDE!\033[m')
print('PARA A COR \033[;33m AMARELA!\033[m')
print('PARA A COR \033[;34m AZUL!\033[m')
print('PARA A COR \033[0;35m ROXA!\033[m')
print('PARA A COR \033[;36m CIANO!\033[m')
print('PARA A COR \033[;90m PRETA\033[m')

==========================================  AULA 17 =====================================================

list = [210,219,230,2]

# list.append( ) Adiciona um numero na lista list.extend( ) e o melhor para add na lista!

# list.sorted coloca a lista em ordem crescente

#list.insert(1, 211) na posicao 1 ele vai trocar o numero 219 pelo 211
 
# list.pop(1) ele vai eliminar o caractere 1 da lista (e melhor usar o list.remove() e colocar qual o numero que eliminar) 

for c ,v in enumerate(list):
    print(f'Na posicao {c} esta o valor {v} ')