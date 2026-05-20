# pedra papel tezoura com tkinter
import tkinter as tk
from random import randint

janela=tk.Tk()
janela.title("pedra,papel ou tezoura")

def jogo():
    global vitoria_do_bot
    global vitoria_do_jogador
    global empate
        
    bot=randint(0,2)
    jogador=escolha_do_jogador.get()
    
    
    if bot==jogador:
        empate+=1
        texto_principal.config(text=f"bot escolheu: {escolhas[bot]}\njogador  escolheu: {escolhas[jogador]}\nresultado: empate")
        
    elif bot==0 and jogador==1:
        vitoria_do_jogador+=1
        texto_principal.config(text=f"bot escolheu: {escolhas[bot]}\njogador  escolheu: {escolhas[jogador]}\nresultado: jogador vence")
        
    elif bot==0 and jogador==2:
        vitoria_do_bot+=1
        texto_principal.config(text=f"bot escolheu: {escolhas[bot]}\njogador  escolheu: {escolhas[jogador]}\nresultado: bot vence")
        
        
    elif bot==1 and jogador==0:
        vitoria_do_bot+=1
        texto_principal.config(text=f"bot escolheu: {escolhas[bot]}\njogador  escolheu: {escolhas[jogador]}\nresultado: bot vence")
        
        
    elif bot==1 and jogador==2:
        vitoria_do_jogador+=1
        texto_principal.config(text=f"bot escolheu: {escolhas[bot]}\njogador  escolheu: {escolhas[jogador]}\nresultado: jogador vence")
        

    elif bot==2 and jogador==0:
        vitoria_do_jogador+=1
        texto_principal.config(text=f"bot escolheu: {escolhas[bot]}\njogador  escolheu: {escolhas[jogador]}\nresultado: jogador vence")
        

    elif bot==2 and jogador==1:
        vitoria_do_bot+=1
        texto_principal.config(text=f"bot escolheu: {escolhas[bot]}\njogador  escolheu: {escolhas[jogador]}\nresultado: bot vence")
        
    pontuacao.config(text=f"empate:[{empate}]\nvitoria do jogador:[{vitoria_do_jogador}]\nvitoria do bot:[{vitoria_do_bot}] ")


def verificar_resposta():
    if escolha_do_jogador.get() in (0,1,2):
        texto_principal.config(text="opcao valida!")
        jogo()
    else:
        texto_principal.config(text="por favor escolha uma opcao")


def fecho():
    janela.destroy()


escolhas=("pedra","papel","tezoura")
empate=0
vitoria_do_bot=0
vitoria_do_jogador=0

texto_principal=tk.Label(janela,text="esse e um jogo de pedra panel e tezora")
texto_principal.pack()

escolha_do_jogador=tk.IntVar()
tk.Radiobutton(janela, text="pedra", variable=escolha_do_jogador, value=0).pack()
tk.Radiobutton(janela, text="papel", variable=escolha_do_jogador, value=1).pack()
tk.Radiobutton(janela, text="tezora", variable=escolha_do_jogador, value=2).pack()

botao_de_envio=tk.Button(janela,text="enviar",command=verificar_resposta)
botao_de_envio.pack()

pontuacao=tk.Label(text="aqui fica a pontuacao")
pontuacao.pack()

botao_de_fecho=tk.Button(text="fechar",command=fecho).pack()

janela.mainloop()
