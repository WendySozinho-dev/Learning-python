#exercicio98
from time import sleep
def contador(inicio,fim,passo):
    if passo ==0:
        passo=1
    elif passo <0:
        passo*=-1
    cont=inicio
    if inicio <=  fim:
        while  cont <= fim:       
            print(cont,end=" ",flush=True)
            sleep(0.4)
            cont+=passo
        print()
    else:
        while cont > fim:
            sleep(0.4)
            print(cont,end=" ",flush=True)
            cont+=-passo
        print(fim)
        print()


print("contagem de 1 a 10 de 1 em 1")
print("--"*20)
contador(1,10,1)
print("contagem de 10 a 1 de 2 em 2")
print("--"*20)
contador(10,1,2)
print("sua vez")
inicior=int(input("inicio "))
fimr=int(input("fim  "))
passor=int(input("passo  "))
contador(inicior,fimr,passor)
