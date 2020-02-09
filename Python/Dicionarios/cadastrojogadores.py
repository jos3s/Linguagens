time=[]
jogador={}
partidas=[]
while True:
    jogador.clear()
    jogador['nome']=str(input('Nome:'))
    nj=int(input('Numero de jogos: '))
    partidas.clear()
    for c in range(0,nj):
        partidas.append(int(input(f'Quantos gols na partida {c}:')))
    jogador['gols']=partidas[:]
    jogador['total']=sum(partidas)
    time.append(jogador.copy())
    while True:
        resp=str(input('Quer continuar: [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Erro')
    if resp =='N':
        break
   
   
print('='*30)
print('cod',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('='*30)

while True:
    busca=int(input('Mostra dado de qual jogador?'))
    if busca==999:
        break
    if busca>=len(time):
        print('Erro, jogador não encontrado')
    else:
        print(f'Levantamento do jogador {time[busca]["nome"]}')
        for i,g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i} fez {g} gols')

''' print('='*30)    
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i} foram {v} gols') '''

''' print(jogador)
print('='*30)    
for k, v in jogador.items():
    print(f'{k} tem valor {v}') '''