import requests
from tkinter import * 
from functools import partial


def exibir(btn):
    request=requests.get("https://api.hgbrasil.com/finance/quotations?key=bd652b81")
    data=request.json()
    currencies=('USD','EUR','GBP','ARS','BTC')
    if btn==bt1:
        dataMoney=data['results']['currencies']["USD"]
        lb1['text']='Moeda: '+str(dataMoney['name'])
        lb2['text']='Compra: ' +str(dataMoney['sell'])
        lb3['text']='Venda: '+str(dataMoney['buy'])
        lb4['text']='Variação: '+str(dataMoney['variation'])
    elif btn==bt2:
        dataMoney=data['results']['currencies']["EUR"]
        lb1['text']='Moeda: '+str(dataMoney['name'])
        lb2['text']='Compra: ' +str(dataMoney['sell'])
        lb3['text']='Venda: '+str(dataMoney['buy'])
        lb4['text']='Variação: '+str(dataMoney['variation'])
    elif btn==bt3:
        dataMoney=data['results']['currencies']["ARS"]
        lb1['text']='Moeda: '+str(dataMoney['name'])
        lb2['text']='Compra: ' +str(dataMoney['sell'])
        lb3['text']='Venda: '+str(dataMoney['buy'])
        lb4['text']='Variação: '+str(dataMoney['variation'])
    else:
        dataMoney=data['results']['currencies']["BTC"]
        lb1['text']='Moeda: '+str(dataMoney['name'])
        lb2['text']='Compra: ' +str(dataMoney['sell'])
        lb3['text']='Venda: '+str(dataMoney['buy'])
        lb4['text']='Variação: '+str(dataMoney['variation'])


janela=Tk() 

lb1=Label(janela, text=" ")
lb1.place(x=95,y=80)
lb2=Label(janela, text=" ")
lb2.place(x=95,y=95)
lb3=Label(janela, text=" ")
lb3.place(x=95,y=110)
lb4=Label(janela, text=" ")
lb4.place(x=95,y=125)


bt1=Button(janela,width=10, text="USD")
bt1['command']=partial(exibir,bt1)
bt1.place(x=70,y=170)
bt2=Button(janela,width=10, text="EUR")
bt2['command']=partial(exibir,bt2)
bt2.place(x=170,y=170)
bt3=Button(janela,width=10, text="ARS")
bt3['command']=partial(exibir,bt3)
bt3.place(x=70,y=200)
bt4=Button(janela,width=10, text="BTC")
bt4['command']=partial(exibir,bt4)
bt4.place(x=170,y=200)

janela.geometry("300x300+100+100")
janela.mainloop()
 
