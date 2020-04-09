def aumentar(preco=0,taxa=0, form=False):
    res=preco+(preco*taxa/100)
    return res if form is False else moeda(res)
    
    
def diminuir(preco=0,taxa=0,form=False):
    res=preco-(preco*taxa/100)
    return res if form is False else moeda(res)
    
    
def dobro(preco=0,form=False):
    res=preco*2
    return res if form is False else moeda(res)
  
    
def metade(preco=0,form=False):
    res=preco/2
    return res if form is False else moeda(res)

def moeda(preco=0,moeda='RS'):
    return f'{moeda}{preco:.2f}'.replace('.',',')


def exibir(preco,taxaA=10,taxaD=10,form=True):
    print('Resumo do valor')
    print(f'Preço: \t\t\t{moeda(preco)}')
    print(f'Metade: \t\t{metade(preco,form)}')
    print(f'Dobro: \t\t\t{dobro(preco,form)}')
    print(f'Aumento de {taxaA}%: \t{aumentar(preco,taxaA,form)}')
    print(f'Diminuição de {taxaA}%: \t{diminuir(preco,taxaD,form)}')