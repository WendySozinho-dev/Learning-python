#exercicio99
def maior(lista):
    list=lista[:]
    list.sort()
    print(f"digitou {list} e o maior valor e {list[-1]}")


numeros=[]
while True:
    n=int(input("digite um valor  "))
    numeros.append(n)
    cont=input("quer continuar? [s/n]  ")
    if cont=="n":
        break
maior(numeros)
