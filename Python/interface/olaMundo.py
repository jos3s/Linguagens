from Tkinter import * 
from functools import partial

def btnClick(bt):
    if bt==bt1:
        lb['text']="Hello Word"
    elif bt==bt2:
        lb['text']="Hola Mundo"
    else:
        lb['text']="Ola mundo"

janela=Tk() 
''' janela.title("Hello Word") '''

lb=Label(janela, text="")
lb.place(x=95,y=100)

bt1=Button(janela,width=20, text="Clique aqui")
bt1['command']=partial(btnClick, bt1)
bt1.place(x=90,y=120)

bt2=Button(janela,width=20, text="Clique aqui")
bt2['command']=partial(btnClick, bt2)
bt2.place(x=90,y=150)

bt3=Button(janela,width=20, text="Clique aqui")
bt3['command']=partial(btnClick, bt3)
bt3.place(x=90,y=180)

janela.geometry("300x300+100+100")
janela.mainloop()