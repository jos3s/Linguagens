def fatorial(num, show=False):
    """
    → Função para calcular o fatorial de um número
    :param num: número que terá o seu fatorial calculado
    :param show: se True, mostra a sequência do cálculo
    :return: impressão do resultado
    """
    f=1
    for c in range(num,0,-1):
        if show:
            print(f'{c} {"x " if c>1 else "="}', end='')
        f*=c
    return f
    
    
num=int(input('Digite o numero: '))
print(f'{fatorial(num,show=True)}')
