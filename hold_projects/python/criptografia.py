from itertools import permutations
import random

letras={"a":("#","?","e","5","t","s","1"),"b":"eeg7@#?"}
letra_binario=letras["a"]
letra_crip=permutations(letra_binario)
lista_letras=[]


cont=0


for c in letra_crip:
    lista_letras.append(c)
    print(c)
print(lista_letras)    



letracrip=random.choice(lista_letras)
for c in letracrip:
    print(c,end="")
print()


descriptografia=permutations(letracrip)

for c in descriptografia:
    
    if c==letras["a"]:
        print("a")
        break  



