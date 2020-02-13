def leiaInt(msg):
    while True:
        try:
            num=int(input(f'{msg}'))
        except (ValueError, TypeError):
            print("\033[31mValor digitado inválido\033[m")
            continue
        except (KeyboardInterrupt):
            print("\nO usuário cancelou a entrada de dado")
            return 0
        else:
            return num
    

def leiaFloat(msg):
    while True:
        try:
            num=float(input(f'{msg}'))
        except (ValueError, TypeError):
            print("\033[31mValor digitado inválido\033[m")
            continue
        except (KeyboardInterrupt):
            print("\nO usuário cancelou a entrada de dado")
            return 0
        else:
            return num
    
    
    
n=leiaInt('Digite um numero inteiro: ')
print(f'{n}')
r=leiaFloat('Digite um numero real: ')
print(f'{r}')
