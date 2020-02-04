l1=int(input('Digite um valor: '))
l2=int(input('Digite um segundo valor: '))
l3=int(input('Digite um terceiro valor: '))

if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    if l1 == l2 == l3:
        print('Os valores podem formar um triangulo e ele é um equilátero')
    elif l1==l2 or l2==l3:
        print('Os valores  podem formar um triangulo e ele é um isóceles')
    else:
        print('Os valores podem formar um triangulo e ele é um escaleno')
else:
    print('Os valores não podem formar um triangulo')