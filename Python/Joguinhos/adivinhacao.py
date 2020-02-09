from random import randint
num=randint(1,10)
n=0
cont=0
while n!=num:
    n=int(input('Digite um numero: '))
    if num == n:
        cont+=1
        print('Você acertou e precisou de {} tentivas' .format(cont))
    else:
        cont+=1
        print('Tente novamente!')