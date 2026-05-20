from random import randint
from ferramentas import *


def lotaria():
    bot=[]
    sorteio=[]
    conteudo=""
    item=0
    testebot=[]
    acerto=[]
    cont=0
    escreva("digite -1 para parar")
    
    while True:
        for c in range(0,5):
            item=randint(0,99)
            bot.append(item)
        for c in range(0,5):
            conteudo=input(f"digite o {c+1} numero\n")
            item=leiaint(conteudo)
            if item<0:
                break
            sorteio.append(item)
        
        if item<0:
            break
    
    
        for c in bot:
            testebot.append(c)
    
        for escolha in sorteio:
            if escolha in testebot:
                acerto.append(escolha)
                testebot.remove(escolha)
            cont+=1 
        escreva("eis os numeros sorteiados")
        print(f"\033[33m{bot}\33[m")
        escreva("eis os numeros que escolheu")
        print(f"\033[33m{sorteio}\33[m")
        escreva(f"eis os numeros que acertou")
        print(f"\033[33m{acerto}\33[m")
    
    escreva("valeu mesmo a pena apostar?")
    escreva("pense nisso")
    escreva("ate mais")
    
    