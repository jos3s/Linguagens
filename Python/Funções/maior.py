from random import randint
def maior(*num):
    cont=maior=0
    for valor in num:
        print(f'{valor} ',end='')
        if maior<valor:
            maior=valor
    print(f', o maior valor é {maior}')    

maior(1,2,3,4,5,6)
maior(4,5,6,3,2,1,8,9,10)
maior()