#exercicio 91
from random import randint
from time import sleep
from operator import itemgetter
jogador={"jogador1":randint(1,6),"jogador2":randint(1,6),"jogador3":randint(1,6),"jogador4":randint(1,6),"jogador5":randint(1,6),"jogador6":randint(1,6)}
for c,v in jogador.items():
    sleep(randint(1,2))
    print(c,"teve",v)
sleep(1)
print("--"*15)
print("eis a pontuacao")
print("--"*15)
ranking=sorted(jogador.items(), key=itemgetter(1), reverse=True )
for c,a in ranking:
    sleep(randint(1,2))
    print(f"{c} teve {a}")
