from random import randint
from operator import itemgetter 
jogo={'jogador1':randint(1,6),
      'jogador2':randint(1,6),
      'jogador3':randint(1,6),
      'jogador4':randint(1,6)}

for k, v in jogo.items():
    print(f'{k} o valor do dado foi {v}')

ranking={}
ranking=sorted(jogo.items(),key=itemgetter(1),reverse=True)
print()
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar : {v[0]} com {v[1]}')