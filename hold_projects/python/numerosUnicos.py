# um programa de cadastro de numeros unicos
list=[]
print("digite -1 para parar")
while True:
    ent=int(input("digite o numero:  "))
    if ent == -1:
       break       
    if ent in list:
        print("numero digitado") 
    list.append(ent)
list.sort()
print(f"eis os numeros digitados {list}")
