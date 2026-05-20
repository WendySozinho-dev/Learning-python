#exercicio 85
tot=[[],[]]
for c in range(0,7):
    ent=float(input("digite um numero  "))
    if ent % 2 == 0:
        tot[0].append(ent)
    else:
        tot[1].append(ent)
tot[0].sort()
tot[1].sort()
print(f"eis a lista dos numeros pares {tot[0]} ")
print("--"*15)
print(f"eis a lista dos numeros impares {tot[1]}")    
