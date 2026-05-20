from classes.jogador import jogador
from classes.inimigo import inimigo
from time import sleep

inimigo=inimigo(1)
jogador=jogador()


while True:
    
    dano_jogador=jogador.atacar()
    print("player")
    print(dano_jogador)
    inimigo.dano_inimigo(dano_jogador)
    if inimigo.vitalidade()<=0:
        print("player wins")
        break
    
    sleep(0.3)
    print("enemy")
    print(inimigo.vitalidade())


