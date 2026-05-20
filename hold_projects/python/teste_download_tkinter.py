
import tkinter as tk

janela = tk.Tk()

texto_principal = tk.Label(text="O seu download estará pronto em")
texto_principal.pack()

contagem_decrescente = tk.Label(text="10")
contagem_decrescente.pack()

def contagem(numero=10):
    if numero > 0:
        contagem_decrescente.config(text=numero)
        janela.after(1000, contagem, numero-1)
    else:
        texto_principal.config(text="O download está pronto!")

botao = tk.Button(text="Clique aqui", command=contagem)
botao.pack()

janela.mainloop()