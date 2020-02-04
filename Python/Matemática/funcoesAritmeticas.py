def soma(a,b):
    return a+b

def div(a,b):
    if a<b:
        return b/a
    else:
        return a/b
    
def mult(a,b):
    return a*b

def sub(a,b):
    if a<b:
        return b-a
    else:
        return a-b
    

a=int(input("Digite um numero: "))
b=int(input("Digite um numero: "))

print('Soma: {} e Divisão: {}\nMultiplicação: {} e Subtração: {}' .format(soma(a,b), div(a,b), mult(a,b), sub(a,b)))
      
      