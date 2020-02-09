from random import randint
def sortear(lista):
    for c in range(0,5):
        lista.append(randint(0,10))
    
    
def somarpares(lista):
    s=0
    for n in lista:
        if n%2==0:
            s+=n
    print(f'A soma dos numeros pares foi {s}')

num=[]
sortear(num)
print(num)
somarpares(num)