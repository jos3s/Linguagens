lista = ('Lapis', 1,
         'Borracha',2,
         'Caderno', 25.90)
print(f'{"Listagem de Preços":^40}')
for pos in range(0, len(lista)):
    if pos%2==0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'RS {lista[pos]:>5.2f}')