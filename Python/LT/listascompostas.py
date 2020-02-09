galera=list()
info=list()
for c in range(0,3):
    info.append(str(input('Nome: ')))
    info.append(int(input('Idade: ')))
    galera.append(info[:])
    info.clear()

print(galera)
''' dados=list()
dados.append('Gustavo')
dados.append(20)

pessoas=list()
pessoas.append(dados[:])

dados[0]='Carlos'
dados[1]=16
pessoas.append(dados[:])

print(pessoas[0][0])
print(pessoas) '''

'''  pessoas=[['João', 19],['Bruna', 34],['Amanda',21]]'''

