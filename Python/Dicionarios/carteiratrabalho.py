from datetime import datetime
dado={}
dado['nome']=str(input('Nome:'))
nasc=int(input('Ano de nascimento:'))
dado['idade']=datetime.now().year-nasc
dado['ctps']=int(input('Carteira de trabalho [0 se não tiver]: '))
if dado['ctps'] != 0:
    dado['contratacao']=int(input('Ano de contratação: '))
    dado['salario']=float(input('Salário: '))
    dado['aposentadoria']= dado['idade'] +((dado['contratacao'] +35) - datetime.now().year)

for k,v in dado.items():
    print(f'{k} tem o valor {v}')
