#jogo de azar
from random import randint
from ferramentas import *
from ppt3 import ppt3
from adivinha import adivinha
from lotaria import lotaria

comandos=["sair do jogo","pedra, papel ou tezora","xindondinha","lotaria"]

while True:
    menu(comandos)
    conteudo=input("digite o comando\n")
    entrada=leiaint(conteudo)
    confirmacao=existe(entrada,comandos)
    while not confirmacao:
        escreva("opcao inexistente")
        conteudo=input("tente novamente\n")
        entrada=leiaint(conteudo)
        confirmacao=existe(entrada,comandos)
    
    if entrada==1:
        escreva("ate mais")
        break
    elif entrada==2:
        ppt3()
    elif entrada==3:
        adivinha()
    elif entrada==4:
        lotaria()
