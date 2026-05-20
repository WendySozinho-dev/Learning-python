from random import randint
from time import sleep
from ferramentas import*

def ppt3():
    escolha=("pedra","papel","tezora")
    escreva("digite -1 para parar")
    conteudo=""
    entrada=0
    while True:
        bot=randint(0,2)
        menu(escolha)
        conteudo=input()
        entrada=leiaint(conteudo)
        confirmacao=existe(entrada,escolha)
        while not confirmacao:
            if entrada<0:
                break
            escreva("opcao inexistente :(")
            conteudo=input("\33[32mtente novamente\33[m  ")
            entrada=leiaint(conteudo)
            confirmacao=existe(entrada,escolha)
    
        if   entrada<0:
            break      
        entrada1=entrada-1
        if entrada1==bot:
            escreva(f"player: {escolha[entrada1]}")
            escreva(f"bot: {escolha[bot]}")
            sleep(0.5)
            escreva("bot: empatamos")
            sleep(2)
    
        elif entrada1==0 and bot==1:
            escreva(f"player: {escolha[entrada1]}")
            escreva(f"bot: {escolha[bot]}")
            sleep(0.5)
            escreva("bot: ganhei")
            sleep(2)
        
        elif entrada1==0 and bot==2:
            escreva(f"player: {escolha[entrada1]}")
            escreva(f"bot: {escolha[bot]}")
            sleep(0.5)
            escreva("player: ganhei")
            sleep(2)
        
        elif entrada1==1 and bot==0:
            escreva(f"player: {escolha[entrada1]}")
            escreva(f"bot: {escolha[bot]}")
            sleep(0.5)
            escreva("player: ganhei")
            sleep(2)
    
        elif entrada1==1 and bot==2:
            escreva(f"player: {escolha[entrada1]}")
            escreva(f"bot: {escolha[bot]}")
            sleep(0.5)
            escreva("bot: ganhei")
            sleep(2)
    
        elif entrada1==2 and bot==0:
            escreva(f"player: {escolha[entrada1]}")
            escreva(f"bot: {escolha[bot]}")
            sleep(0.5)
            escreva("bot: ganhei")
            sleep(2)
    
        elif entrada1==2 and bot==1:
            escreva(f"player: {escolha[entrada1]}")
            escreva(f"bot: {escolha[bot]}")
            sleep(0.5)
            escreva("player: ganhei")
            sleep(2)
    




