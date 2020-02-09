from random import randint
lista=[]
jogos=[]
quant=int(input('Digite a quantidade de jogos que você quer: '))
for n in range(0, quant):
    cont=0
    while True:
        num=randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont>=6:
            lista.sort()
            break
    jogos.append(lista[:])
    lista.clear()

for i,l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    