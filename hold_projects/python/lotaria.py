#lotaria
from time import sleep
from random import randint
list=[]
print("--"*5,"lotaria","--"*5)
ent=int(input("quantos jogos queres sortear? "))
for c in range(0,ent):
    cont=[]
    for a in range(0,6):
        item=(randint(0,60))
        cont.insert(0,item)
    cont.sort()
    list.append(cont[:])
print("~~"*15)
print("eis o sorteio")
print("--"*15)
for c in list:
    sleep(1)
    print(c)
print("--"*15)
