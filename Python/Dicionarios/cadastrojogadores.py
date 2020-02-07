jogador={}
partidas=[]
jogador['nome']=str(input('Nome:'))
nj=int(input('Numero de jogos: '))
for c in range(0,nj):
    partidas.append(int(input(f'Quantos gols na partida {c}:')))
jogador['gols']=partidas[:]
jogador['total']=sum(partidas)

print(jogador)
print('='*30)    
for k, v in jogador.items():
    print(f'{k} tem valor {v}')
   
print('='*30)    
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i} foram {v} gols')
