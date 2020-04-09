def ficha(jog='<desconhecido>', gols=0):
    print(f'O nome do jogador é {jog} e o numero de gols é {gols}')
        
nome=str(input('Nome:'))
numg=str(input('Numero de gols:'))
if numg.isnumeric():
    numg=int(numg)
else:
    numg=0
if nome.strip() =='':
    ficha(gols=numg)
else:
    ficha(nome,numg)
