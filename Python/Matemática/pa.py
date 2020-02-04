termo = primeiro=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razao: '))

"""for c in range(primeiro,primeiro+(razao*10),razao):
    print('{}'. format(c), end=' -> ')
print('Fim')"""

mais=10
cont=1
total=0
while mais!=0:
    total+=mais
    while cont<=total:
        print('{} '. format(cont), end='')
        termo+=razao
        cont+=1
    mais=int(input('\nQuantos termos a mais você quer ver?'))  
print('Foram mostrados {} termos'.format(cont))
      