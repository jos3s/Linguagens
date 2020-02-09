valores=[]
pares=[]
impares=[]
while True:
    valores.append(int(input('Digite um valor: ')))
    opc=str(input('Quer continuar? [S/N] '))
    if opc in 'Nn':
        break
    
for i,v in enumerate(valores):
    if v%2==0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Os valores digitados foram {valores}')
print(f'Os valores pares digitados foram {pares}')
print(f'Os valores impares digitados foram {impares}')