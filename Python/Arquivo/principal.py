from bib.interface import *
from bib.arquivo import *


arq='\\Users\\julis\\Documents\\GitHub\\Linguagens\\Python\\Arquivo\\arquivo.txt'
if not arqExiste(arq):
    criarArq(arq)
    
    
while True:
    resp=menu(['Cadastra pessoas','Listar pessoas','Sair do sistema'])
    if resp==1:
        texto('Cadastrar pesoas')
        
    elif resp==2:
        lerArq(arq)
    else:
        print('Sistema encerrado')
        break