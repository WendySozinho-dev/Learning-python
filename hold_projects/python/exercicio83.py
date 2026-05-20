#exercicio 83
tot=[]
conteudo=[]
somador=0
comparador=[]
while True:
    nome=input("qual e o nome:    ")
    peso=int(input("qual e o peso:   "))
    conteudo.append(nome)
    conteudo.append(peso)
    comparador.append(peso)
    tot.append(conteudo[:])    
    del conteudo[:]
    somador+=1
    cont=input("quer continuar? S/N   ")    
    if cont in "Nn":
        break
print("--"*15)
print(f"ao todo foram cadastradas {len(tot)}")
print("=-"*20)
for c in range(0,somador):
    print(f"{tot[c][0]} tem {tot[c][1]} kilos")
print("-="*20)
print("lista dos/as mais leves")
comparador.sort()
for c in tot:
    for itens in c:
        if comparador[0] == itens:
            print(f"{c[0]} com {c[1]} kilos")
print("*-"*15)
print("lista dos mais pesados")
print("-*"*15)
for c in tot:
        for itens in c:
            if comparador[-1] == itens:
                print(f"{c[0]} com {c[1]} kilos ")    
        