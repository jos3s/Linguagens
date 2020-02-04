lista=[]
menor=maior=0
for c in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {c}:')))
    if c==0:
        maior=menor=lista[c]
    else:
        if lista[c] > maior:
            maior=lista[c]
        if lista[c] <menor:
            menor=lista[c]  
print(f'Valores {lista}')
print(f'Maior valor é {maior}, nas posições: ', end='')
for i,v in enumerate(lista):
    if v==maior:
        print(f'{i} ', end='')
print(f'\nMenor valor é {menor}, nas posições: ', end='')
for i,v in enumerate(lista):
    if v==menor:
        print(f'{i} ', end='')
#print(f'Menor valor é {min(lista)} e o maior valor é {max(lista)}')

