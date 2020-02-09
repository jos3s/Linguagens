temp=[]
princ=[]
maior=menor=0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    if len(princ)==0:
        maior=menor=temp[1]
    else:
        if temp[1]>maior:
            maior=temp[1]
        if temp[1]<menor:
            menor=temp[1]
    princ.append(temp[:])
    temp.clear()
    opc=str(input('Quer continuar? [S/N]'))
    if opc in 'Nn':
        break

print(princ)
print(f'A lista tem {len(princ)} pessoas cadastradas')
print(f'O maior peso foi {maior} ',end='')
for p in princ:
    if p[1]==maior:
        print(f'[{p[0]}]', end='')
print(f'\nO menor peso foi {menor} ', end='')
for p in princ:
    if p[1]==menor:
        print(f'[{p[0]}]', end='')
