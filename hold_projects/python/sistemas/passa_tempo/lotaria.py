from ferramentas import*
from random import randint

comandos=("sair do jogo","comprar bilhetes","apostar","verificar bilhetes","guardar o registro","informacao sobre o jogo")
ajuda=("sobre a aposta","sobre guardar o registro","sobre os bilhetes")
bilhetes=0


while True:
    menu(comandos,cabecalho="sistema")
    conteudo=input("digite a opcao\n")
    entrada=leiaint(conteudo)
    confirmacao=existe(entrada,comandos)
    while not confirmacao:
        conteudo=input("opcao inexistente tente novamente :(\n")
        entrada=leiaint(conteudo)
        confirmacao=existe(entrada,comandos)

    if entrada==1:
        escreva("ate mais")
        break

    elif entrada==2:
        escreva("insira o numero de bilhetes a comprar max[10]")
        conteudo=input()
        entrada=leiaint(conteudo)
        if entrada<0:
                entrada*=-1
        while entrada>10:
            escreva(f"tentou comprar {entrada} bilhetes max[10]")
            conteudo=input()
            entrada=leiaint(conteudo)
            if entrada<0:
                entrada*=-1
        bilhetes+=entrada
        escreva(f"comprou {entrada} bilhetes")

    elif entrada==3:
        bot1=bot2=bot3=bot4=bot5=[]
        bilhetes_apostados=numero_de_jogos=0
        escreva("quantos biletes em jogo? max[5]")
        conteudo=input()
        entrada=leiaint(conteudo)
        if entrada<0:
            entrada*=-1
        while entrada==0:
            escreva("o sistema detectou um cacata")
            escreva("cacatas nao podem apostar no sistema")
            escreva("tente novamente com um numero >0")
            conteudo=input()
            entrada=leiaint(conteudo)
            if entrada<0:
                entrada*=-1
                    
        bilhetes_apostados=entrada
        if bilhetes_apostados>bilhetes:
            escreva(f"bilhetes insuficientes para a aposta tens[{bilhetes}] bilhetes")
        else:
            escreva("quantas appstas? max[5]")
            conteudo=input()
            entrada=leiaint(conteudo)
            if entrada<0:
                entrada*=-1
            while entrada>5:
                escreva("nao pode realizsar [{entrada}] apostas pois o maximo e [5]")
                conteudo=input("tente novamente\n")
                entrada=leiaint(conteudo)
                entrada=leiaint(conteudo)
            #aqui comeca o jogo da lotaria
            
            
            while len(bot1)<5:
                conteudo=randint(1,80)
                bot1.append(conteudo)
            print(bot1)












