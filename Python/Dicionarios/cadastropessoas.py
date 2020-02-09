pessoa={}
galera=[]
idad=media=0
while True:
    pessoa.clear()
    pessoa['nome']=str(input('Nome: '))
    while True:
        pessoa['sexo']=str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MFmf':
            break
        print('Erro')
    pessoa['idade']=int(input('Idade: '))
    idad+=pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        op=str(input('Você quer continuar? [S/N]')).upper()[0]
        if op in 'SN':
            break
        print('Erro')
    if op == 'N':
        break

print(f'Há {len(galera)} pessoas cadastradas.')
media=idad/len(galera)
print(f'A média das idades é {media} anos')
print(f'',end='')
for p in galera:
    if p['sexo']=='F':
        print(f'{p["nome"]}', end='')
print()
for p in galera:
    if p['idade']>=media:
        print(' ',end='')
        for k,v in p.items():
            print(f'{k} = {v}; ',end='')
        print()

