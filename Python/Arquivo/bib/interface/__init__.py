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
    
    
def linha():
    print('~'*20)

def texto(msg):
    linha()
    print(msg.center(20))
    linha()
    

def menu(lista):
    texto('Menu Principal')
    cont=1
    for i in lista:
        print(f'{cont} - {i}')
        cont+=1
    op=leiaInt('Sua opção: ')
    return op