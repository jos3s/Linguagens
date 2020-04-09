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
        for linha in a:
            dado=linha.split(';')
            dado[1]=dado[1].replace('\n','')
            print(f'{dado[0]:<10}{dado[1]:>5} anos')


def cadastrar(arq,nome='desconhecido',idade=0):
    try:
        a=open(arq,'at')
    except:
        print('Houve um erro com a abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever no arquivo')
        else:
            print('Novo registro cadastrado')
            