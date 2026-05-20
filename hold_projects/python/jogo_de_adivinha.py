#um jogo de adivinha
import random2
from time import sleep
print("digite o inicio e o fim {numeros reais} e a maquina ira processar um valor aleatorio depois e so adivinhar o valor")
cont=(1)
x=int(input("inicio  "))   
z=int(input("fim  "))
while cont==(1):    
    res=(random2.randint(x,z))
    sleep(3) 
    print("que numero eu pensei?")    
    ent=int(input())
    if res == ent:
        sleep(3)
        print("parabens acertou ")
    else:
        sleep(3)
        print("errrrrrrrrrrrrou 🤣🤣🤣🤣 o valor que pensei foi",res," 🫵🤣🤣🤣🤣")
    sleep(1.5)    
    print("deseja continuar? 1{sim} 2{nao}")
    cont=int(input()) 
    if cont != (1) :
        sleep(1.5)
        print("ate mais")
    sleep(0.5)  
         