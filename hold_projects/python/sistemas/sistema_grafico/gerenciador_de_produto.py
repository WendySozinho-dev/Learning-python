import tkinter as tk
import ferramentas_graficas as tools

janela=tk.Tk()

janela.title("sistema")


def fechar():
    janela.destroy()
    





close_btn=tk.Button(text="fechar",command=fechar)
close_btn.pack()
























janela.mainloop()
