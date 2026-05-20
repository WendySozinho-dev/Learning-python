#exercicio100
from random import randint
def sorteia(lista):
       for c in range(0,5):
           n=randint(1,5)
           lista.append(n)
       

def somapar(lista):
    cont=0
    cont1=0   
    for c in lista:
        if c%2==0:
            cont+=c
            cont1+=1
    print(f"ao todo foram somados {cont1} numeros pares totalizando {cont}")


list=list()
sorteia(list)
print(list)
somapar(list)
