while True:
    num=int(input('Digite um numero: '))
    if num<0:
        break
    for cont in range(1,11):
        print(f'{num} x {cont} = {num*cont}')
    