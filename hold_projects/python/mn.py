#um programa que mostra maior e menor
num=[]
cont=(0)
cont2=(0)
pos=[]
num2=[]
pos2=[]
pos3=[]
for c in range(0,5):
    ent=int(input(f"digite um numero {cont}:   "))
    cont+=(1)
    num.append(ent)
    pos.append(cont)
num2=num[:]
num2.sort()
print(f"o maior numero digitado foi {num2[4]}")       
print(f"o menor numero digitado foi {num2[0]}")
for c in num:
     if c == num2[0]:
         pos2.append(cont2)     
     if c ==num2[4]:
         pos3.append(cont2)
     cont2+=(1)
print(f"o maior numero apareceu nas posicoes {pos3}")
print(f"o menor numero apareceu nas posicoes {pos2}")
