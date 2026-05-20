#expressoes numericas










variaveis=[]

numeros=[]

entradav=int(input("qual e o maior expoente do x?  "))

for c in range(entradav,0,-1):
    valor=float(input(f"qual e o multiplicador de x^{c}   "))
    if valor!=0:
             
        variaveis.append(valor)
        print(f"{valor}*x^{c} adicionado")
    else:
        print(f"0^{c} deletado")

print(variaveis)



entradan=int(input("quantos numeros simples a adicionar?  "))
for c in range(0,entradan):
    valor=float(input("digite o numero  "))
    if valor!=0:
        numeros.append(valor)
        print(f"{valor} adicionado")
    else:
        print("valor deletado")

print(numeros)











