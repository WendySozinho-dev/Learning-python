#um programa de cadastro
list =[]
while True:
    ent=int(input("digite um valor:  "))
    list.append(ent)
    cont=input("deseja continuar? s/n ")
    if cont.lower()=="n":
        break
list.sort(reverse=True)
print(f"vc digitou {len(list)} numeros")
print(f"aqui esta a lista {list}")
for c in list:
    if c == 5:
        print("existe o valor 5 na lista")
        break
    
