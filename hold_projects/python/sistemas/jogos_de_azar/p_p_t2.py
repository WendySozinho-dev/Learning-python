#pedra papel tezoura parte #2
#iniciando o bot
from time import sleep
from random import randint
def ppt():

    ppt=("pedra","papel","tezora","sair","mostrar resposta","mostrar progresso","mostrar comandos","jogo de adivinha")
    adv=("0","1","2","3","4","5","parar")
    print("~~"*15)
    print("bot pronto digite sair para sair")
    print("~~"*15)
    sleep(1)
    print( "na duvida digite: | mostrar comandos | para ver os comandos extras " )
    print("~~"*15)
    sleep(2)
    empate=(0)
    bvit=(0)
    pvit=(0)
    amostra=(0)
    consulta=(0)
    padvit=(0)
    badvit=(0)
    while True:
        bot=(randint(0,2))
        player=input("pedra papel ou tezora ")
        while not(player.lower() in ppt)  :
                print("x"*20)
                player=(input("tente novamente  "))
           #comandos extras
        if player.lower() == ppt[3]:
            break   
        elif player.lower() == ppt[4]:
            amostra+=(1)
            print(f"bot: eu pensei em {ppt[bot]} ")
        if player.lower() == ppt[5]:
             consulta+=(1)
             print(".."*10)
             print(f"foram {empate} empates")
             print(f"bot ganhou {bvit} vezes")
             print(f"vc ganhou {pvit} vezes")
             print(f"foram {consulta} consultas")
             print(f"foste mostrado {amostra} vezes")
             print("--"*10)
             #texte logico
        if player.lower() == ppt[6]:
            print(f"eis os comandos disponiveis no momento {ppt[3:]}")
        if ppt[bot] == player.lower():
            empate+=(1)
            print("~_"*10)
            print("bot: empatamos")
            print("_~"*10)
        elif ppt[bot] == ppt[1] and player.lower() == ppt[2]:
            pvit+=(1)
            print("_~"*10)
            print(f"bot: escolhi {ppt[bot]} e tu escohleu {player.lower()} ganhaste ")
            print("_~"*10)
        elif ppt[bot] == ppt[1] and player.lower() == ppt[0]:
            bvit+=(1)
            print("_~"*10)
            print(f"bot: escolhi {ppt[bot]} e tu escohleu {player.lower()} ganhei ")
            print("_~"*10)
        elif ppt[bot] == ppt[0] and player.lower() == ppt[1]:
            pvit+=(1)
            print("_~"*10)
            print(f"bot: escolhi {ppt[bot]} e tu escohleu {player.lower()} ganhou ")
            print("_~"*10)
        elif ppt[bot] == ppt[0] and player.lower() == ppt[2]:
            bvit+=(1)
            print("_~"*10)
            print(f"bot: escolhi {ppt[bot]} e tu escohleu {player.lower()} ganhei ")
            print("_~"*10)
        elif ppt[bot] == ppt[2] and player.lower() == ppt[0]:
            pvit+=(1)
            print("_~"*10)
            print(f"bot: escolhi {ppt[bot]} e tu escohleu {player.lower()} ganhou ")
            print("_~"*10)
        elif ppt[bot] == ppt[2] and player.lower() == ppt[1]:
            bvit+=(1)
            print("_~"*10)
            print(f"bot: escolhi {ppt[bot]} e tu escohleu {player.lower()} ganhei ")
            print("_~"*10) 
            #fim do pedra papel tezora e inicio de adivinha
        if player.lower() == ppt[7]:
            print("digite parar para parar")         
            sleep(2.5)
            print("bot2 pronto")
            while True:
                   bot2=(randint(0,5))
                   print("bot2: que numero pensei?")         
                   player2=input("")
                   while not(player2 in adv):                  
                       player2=input("tente novamente   ")
                   if player2.lower()==adv[6]:
                       break    
                   if player2==adv[bot2]:
                       print("~_"*15)
                       print("acertou")
                       print("_~"*15)
                   else:
                       print("~~"*15)
                       print(f"errou eu pensei em {bot2}")
                       print("^^"*15)
                       #fim da adivinha     
    print(".."*10)
    print(f"foram {empate} empates")
    print(f"bot ganhou {bvit} vezes")
    print(f"vc ganhou {pvit} vezes")
    print(f"foram {consulta} consultas")
    print(f"foste mostrado {amostra} vezes") 
    print("--"*10)
                                  