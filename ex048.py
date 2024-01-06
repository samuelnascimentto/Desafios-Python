s = 0
c = 0
for n in range(1,501 ):
    if n % 3 == 0:
        if n % 2 == 1:
            s += n
            c += 1
print('ACABEI!!')
print(f'Existem {c} divisiveis entre 3 e 500 e a soma de todos sera: {s}')
       