#jogo de adivinha
from time import sleep
from random import randint
pontos=10
vitoria=0
derrota=0
while True:
    bot=randint(1,3)
    player=int(input("que numero penei?  "))
    if player==bot:
        pontos+=1
        vitoria+=1
        
        print("--"*10)
        print(f"venceu tens {pontos} pontos")
    else:
        pontos-=1
        derrota+=1
        print("__"*10)
        print(f"perdeu tens {pontos} pontos")
        print(f"pensei em {bot}")
    if pontos<=0:
        print(f"game over tens {pontos} pontos")
        break
print("~"*10)
print(f"vitorias: {vitoria}")
print(f"derrotas: {derrota}")
print("~"*10)
