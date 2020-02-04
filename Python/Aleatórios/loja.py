total=prodmil=prodbarato=cont=0
menorpreco=''
while True:
    prod=input('Nome do produto: ')
    preco=int(input('Preço do produto: '))
    total+=preco
    cont+=1
    esc=input('Quer continuar? S/N ').strip().upper()[0]
    if preco>1000:
        prodmil+=1
    if cont==1 or preco<prodbarato:
        prodbarato=preco
        menorpreco=prod
    if esc in 'N':
        break
    
print(f'O total da compra foi RS {total}')
print(f'Há {prodmil} que custa mais que RS1000')
print(f'O produto mais barato foi {menorpreco} que custou RS{prodbarato}')

    