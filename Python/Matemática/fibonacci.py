num=int(input('Digite a quantidade de termos: '))
f1=0
f2=1
cont=0
while cont<num:
    print('{} {} '.format(f1, '->' if cont<num-1 else '') , end='')
    f3=f1+f2
    f1=f2
    f2=f3
    cont+=1
    