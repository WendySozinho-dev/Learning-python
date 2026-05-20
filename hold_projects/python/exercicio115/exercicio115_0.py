from time import sleep

def escreva(txt):
    for c in txt:
        print("_",end="")
    print()
    print(txt)
    for c in txt:
        print("_",end="")
    print()


def leiaint():
    valor=""
    num=0
    while True:
        try:
            valor=input("digite um numero inteiro   ")
            num=int(valor)
            break
        except:
            print(f"<{valor}> nao e um numero valido")
    return num


def linha(tam=30):
    print("_"*tam)


def menu(item):
    entrada=0
    while True:
        cont=1
        sleep(1.5)
        linha()
        print("menu")
        linha()
        for c in item:
            print(f"{cont}:\033[36m{c}\033[m")
            cont+=1
        linha()
        entrada=leiaint()#verifica se e um numero inteiro
        while entrada>cont or entrada<=0:#verifica se o numero existe no menu
            escreva("numero invalido")
            entrada=leiaint()
        sleep(0.5)
        escreva(f"vc digitou {entrada}:\033[33m{item[entrada-1]}\033[m")    
        