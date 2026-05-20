import tkinter as tk
from random import randint

janela=tk.Tk()
janela.title("a minha janela")


def reescrever():
    numero=randint(0,100)
    label2.config(text="ola mundo")
    label.config(text=numero)

def fechar():
    janela.destroy()


numero=randint(0,100)

label2=tk.Label(text="teste")
label2.pack()
label= tk.Label(janela,text=numero,
                            bg="yellow",
                            fg="#fa0000",
                            font=("Arial",20)
                            
                            
                            )

label.pack()






valor_minimo=tk.Entry(janela,text="valor minimo").pack()

tk.Button(janela,text="clique aqui",command=reescrever).pack()
tk.Button(janela,text="fechar",command=fechar).pack()

janela.mainloop()







