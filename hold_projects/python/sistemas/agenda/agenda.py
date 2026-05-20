from datetime import datetime
from ferramentas import *
from dados.gerenciador import*

comandos=("sair da agenda","agendar","desagendar","mostrar agenda")

while True:
    menu(comandos)
    entrada=leiaint(input("digite o comando\n"))
    confirmacao=existe(entrada,comandos)
    while not confirmacao:
        escreva("opcao inexistente tente novamente :(")
        entrada=leiaint(input("digite o comando\n"))
        confirmacao=existe(entrada,comandos)
    
    if entrada==1:
        break
        
    elif entrada==2:
        escreva("digite o plano")
        plano=organizar(input())
        escreva("digite o ano")
        ano=leiaint(input())
        escreva("digite o mes")
        mes=leiaint(input())
        escreva("digite o dia")
        dia=leiaint(input())
        escreva("digite a hora [-1] para cancelar a hora")
        hora=leiaint(input())

        




