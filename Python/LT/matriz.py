mat=[[0,0,0],[0,0,0],[0,0,0]]
pares=tcoluna=smaior=0
for i in range(0,3):
    for j in range (0,3):    
        mat[i][j]=int(input(f'Digite um valor para posição [{i}, {j}]: '))

for i in range(0,3):
    tcoluna+=mat[i][2]
    if mat[1][i]>smaior:
        smaior=mat[1][i]
    for j in range (0,3):         
        print(f'[{mat[i][j]:^5}]', end='')
        if mat[i][j]%2==0:
            pares+=mat[i][j]
    print()
print()
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da 3 coluna é {tcoluna}')
print(f'O maior valor da 2 linha é {smaior}')
# print(f'O maior valor da 2 linha é {max(mat[1])}')
    