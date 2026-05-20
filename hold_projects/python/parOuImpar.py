#par ou impar com listas
list=[]
impar=[]
par=[]
while True:
    ent=int(input("digite um numero:  "))
    list.append(ent)
    if ent % 2==0:
        par.append(ent)
    else:
        impar.append(ent)
    cont=input("quer continuar s/n  ")
    if cont=="n":
        break
print(f"a lista total e {list}")
print(f"a lista dos numeros impares e {impar}")
print(f"a lista dos numeros pares e {par}")
