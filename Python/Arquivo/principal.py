from bib.interface import *
from bib.arquivo import *

arq='\\Users\\julis\\Documents\\GitHub\\Linguagens\\Python\\Arquivo\\arquivo.txt'
if not arqExiste(arq):
    criarArq(arq)
    
  
while True:
    resp=menu(['Cadastra pessoas','Listar pesso1as','Sair do sistema'])
    if resp==1:
        texto('Cadastrar pesoas')
        texto('Novo cadastro')
        nome=str(input('Nome: '))
        idade=leiaInt('Idade: ')
        cadastrar(arq,nome,idade)
    elif resp==2:
        lerArq(arq)
    else:
        texto('Sistema encerrado')
        break
