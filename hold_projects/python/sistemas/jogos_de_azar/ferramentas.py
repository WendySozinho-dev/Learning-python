def leiaint(valor):
    num=0
    while True:
        try:
            num=int(valor)
        except:
            print(f"{valor} nao e um numero inteiro")
            valor=str(input("tente novamente\n"))
        else:
            return num    


def existe(item,lista):
    valor=leiaint(item)
    caixa=len(lista)
    if valor>0 and valor<=caixa:
        return True
    else:
        return False        


def escreva(txt):
    cont=0
    for c in txt:
       cont+=1 
    linha(cont,"-")
    print(f"\033[33m{txt}\033[m")
    linha(cont)


def linha(param=30,linha="_"):
    for c in range(0,param):
        print(linha,end="")
    print()


def menu(lista):
    cont=1
    escreva("menu")
    linha()
    for c in lista:
        print(f"{cont}:\033[36m{c}\033[m")
        cont+=1
    linha()
