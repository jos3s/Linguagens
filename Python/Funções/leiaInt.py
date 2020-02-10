def leiaInt(msg):
    num=str(input(f'{msg}'))
    if num.isnumeric():
        num=int(num)
        return  num
    else:
        leiaInt(msg)
        
n=leiaInt('Digite um numero: ')
print(f'{n}')
