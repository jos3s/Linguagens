from bib.interface import texto

def arqExiste(nome):
    try:
        a=open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArq(nome):
    try:
        a=open(nome,'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
        
    
def lerArq(nome):
    try:
        a=open(nome,'rt')
    except:
        print('Erro na leitura do arquivo')
    else:
        texto('Pessoas cadastradas')
        print(a.readlines())