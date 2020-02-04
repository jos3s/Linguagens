c = num=int(input('Digite um numero: '))
fat=1
print('O fatorial de {} é: '.format(num))
while c>0:
    print('{} {} '.format(c, 'x' if c>1 else '='), end='')
    fat*=c
    c-=1
print('{}'.format(fat))
