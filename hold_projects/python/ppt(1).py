#pedra,papel,tezoura
from random import randint
cont=(1)
while cont == 1:
    ppt=("pedra","papel","tezoura")
    bot=(randint(0,2))
    player=input("pedra papel ou tezoura  ")
    while True:
        if player.lower() in ppt:
            break
        else:
            print("x"*20)
            player=(input("tente novamente  ")) 
            print("x"*20)
    if ppt[bot] == player:
        print("^"*15)
        print("acertou")
        print("-"*15)
    else:
        print("~"*15)
        print(f"errou, foi {ppt[bot]}")
        print("."*15)
    cont=int(input("quer continuar? 1~sim 2~nao  "))         
