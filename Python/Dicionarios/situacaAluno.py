aluno={}
aluno['nome']=str(input('Nome: '))
aluno['media']=float(input('Média: '))
if aluno['media']>=7:
    aluno['situção']='aprovação'
elif 5<=aluno['media']:
    aluno['situção']='recuperação'
else:
    aluno['situção']='reprovação'

for k,v in aluno.items():
    print(f'{k} é de {v}')
    