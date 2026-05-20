#critografia2
from itertools import permutations
import random


letra_binaria={"a":"01100001"}


letra_permutada=permutations(letra_binaria["a"])
lista_de_letra_permutada=[]
letra=""
letra_escolhida=""
chave=0
cont=0



#criptografia
for c in letra_permutada:
    for a in c:
        letra+=a
    lista_de_letra_permutada.append(letra)
    letra=""
letra_escolhida=random.choice(lista_de_letra_permutada)


#chave da criptografia
for c in lista_de_letra_permutada:
    cont+=1
    if letra_escolhida==c:
        print(cont,letra_escolhida)
        break


