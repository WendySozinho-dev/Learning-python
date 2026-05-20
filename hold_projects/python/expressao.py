#exercicio 83
list=[]
cont=0
cont2=0
ent=input("digite sua expressao: ")
list.append(ent)
for c in list:
    for partes in c:
        if "(" in partes:
            cont+=1
        elif ")" in partes:
            cont2+=1    
if  cont == cont2:
    print("sua expressao esta correcta")
else:
    print("sua expressao esta errada")    
