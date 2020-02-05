ficha=[]
boletim=[]
while True:
    nome=str(input('Nome:'))
    n1=float(input('Nota 1:'))
    n2=float(input('Nota 2:'))
    media=(n1+n2)/2
    ficha.append([nome,[n1,n2], media])
    op=str(input('Quer continuar? [S/N]:'))
    if op in 'Nn':
        break

print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print()
for i,a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

print()
while True:
    opc=int(input('Mostrar notas de qual aluno? [999 interrompe]'))
    if opc==999:
        break
    if opc<=len(ficha)-1:
        print(f'As notas de {ficha[opc][0]} são {ficha[opc][1]}')