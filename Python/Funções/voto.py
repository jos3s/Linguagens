def voto(ano):
    from datetime import date
    atual=date.today().year
    idade=atual-ano
    if idade<16:
        return f'{idade} anos: Não vota'
    elif 16<=idade<18 or idade>65:
        return f'{idade} anos: Voto opcional'
    else:
        return f'{idade} anos: Voto obrigatório'
ano=int(input('Digite o seu ano de nascimento: '))
print(voto(ano))
