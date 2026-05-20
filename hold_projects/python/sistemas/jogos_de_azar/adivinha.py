from random import randint
from ferramentas import *
def adivinha():
    bot=0
    conteudo=""
    escreva("digite -1 para parar")
    conteudo=input("digite o numero limite da adivinha\n")
    limite=leiaint(conteudo)
    moeda=10
    vitoria=0
    derrota=0
    vitoria1=0
    while True:
        if limite<0:
            break
        bot=randint(0,limite)
        conteudo=input("tente adivinhar o numero\n")
        entrada=leiaint(conteudo)
        moeda-=1
    
        if moeda<=0:
            escreva("estas txonado digite o numero de moedas que queres")
            conteudo=input()
            moeda=leiaint(conteudo)
            while moeda<=0:
                escreva("nao podes roubar a xindondinha adicione mais moedas")
                conteudo=input()
                moeda=leiaint(conteudo)
                
        if entrada<0:
            break
                    
        if entrada==bot:
            moeda+=1*limite
            vitoria+=5*limite
            vitoria1=5*limite
            escreva(f"parabens venceu +{vitoria1}mt")
        else:
            escreva(f"o valor escolhido foi {bot}")
            escreva(f"perdeu tente novamente -5mt")
            derrota+=5
    
    escreva(f"ganhaste {vitoria} meticais")
    escreva(f"perdeste {derrota} meticais")
    lucro=vitoria-derrota
    escreva(f"o seu lucro foi de {lucro} meticais, sera que valeu a pena?")
   