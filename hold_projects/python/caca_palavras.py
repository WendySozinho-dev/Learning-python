#caca palavras
from itertools import permutations
#gracas a google
while True:
    list=[]
    nletras=int(input("quantas letras  "))
    for c in range(0,nletras):
        letra=str(input(f"a {c+1} letra  "))
        list.append(letra)
    palavra=permutations(list)
    print(list)
    for c in palavra:
        print(     "==>",c)
        print("--"*20)
        print(" ")
