def notas(*n,situ=False):
    r={}
    r['total']=len(n)
    r['maior']=max(n)
    r['menor']=min(n)
    r['media']=sum(n)/len(n)
    if situ:
        if r['media'] >=7:
            r['situação']='Boa'
        elif r['media'] >=5:
            r['situação']='Razoável'
        else:
            r['situação']='Ruim'     
    return r


result=notas(5.6,4.7,8,situ=True)
print(result)