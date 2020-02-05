lista=[[],[]]
for n in range(1,8):
    valor=int(input(f'Digite o {n} valor: '))
    if valor%2==0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

lista[0].sort()
lista[1].sort()
print(f'Todos os valores {lista}')
print(f'Os valores pares são {lista[0]}')
print(f'Os valores ímpares são {lista[1]}')