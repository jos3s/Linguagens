estados={}
brasil=[]
for c in range(0,2):
    estados['nome']=str(input('Nome do estado:'))
    estados['universidade']=str(input('Faculdade: '))
    brasil.append(estados.copy())
    
print(brasil)

for e in brasil:
    for k,v in e.items():
        print(f'{k} {v}')

""" brasil=[]
pe={'uf':'PE', 'faculdade':'UPE'}
ce={'uf':'CE', 'faculdade':'UFC'}
brasil.append(pe)
brasil.append(ce)

print(brasil)
print(brasil[0]['uf']) """

""" pessoas={'nome':'Jose', 'idade':18}
pessoas['nome']='luis'
pessoas['peso']=65
print(f'O {pessoas["nome"]} tem {pessoas["idade"]}')
# print(pessoas.keys())
# print(pessoas.items())
# print(pessoas)

for k,v in pessoas.items():
    print(f'{k}={v}') """