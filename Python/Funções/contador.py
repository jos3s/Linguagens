def contador(i,f,p):
    if p<0:
        p*=-1
    if p==0:
        p=1
    
    if i<f:
        cont=i
        while cont<=f:
            print(f'{cont} ',end='')
            cont+=p
        print()
    else:
        cont=i
        while cont>=f:
            print(f'{cont} ',end='')
            cont-=p
        print()
    
    
contador(1,10,1)
contador(int(input('Inicio:')), int(input('Fim:')), int(input('Passo:')))