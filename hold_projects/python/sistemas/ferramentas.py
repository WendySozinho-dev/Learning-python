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


def menu(lista,cabecalho="menu",contador=(0),espaco=""):
    cont=0
    escreva(cabecalho)
    try:        
        cont=int(contador)
        cont=1
        linha()
        for c in lista:
            print(f"{cont}:\033[36m{c}\033[m")
            cont+=1
        linha()
    except:
        linha()
        cont=0
        limite=len(contador)
        for c in lista:
            if cont>limite-1:
                cont=0
            
            
            print(f"{contador[cont]}:{espaco}\033[36m{c}\033[m")
            cont+=1
            
            
        linha()    


def leiareal(valor):
    num=0
    while True:
        try:
            num=float(valor)
        except:
            print(f"{valor} nao e um numero inteiro")
            valor=str(input("tente novamente\n"))
        else:
            return num    

def sexo(sexo):
    if sexo=="M" or sexo=="m" or sexo=="F" or sexo=="f":
        escreva("sucesso")
        return sexo
    else:
        while not(sexo=="M" or sexo=="m" or sexo=="F" or sexo=="f"):
            sexo=input("tente novamente\n")


def organizar(txt,espacamento="-"):

    b=""
    cont=0
    cont0=0
    for c in txt:
        
        if c!=" ":
                
                b+=c
                cont=0
                cont0=0
        else:
                cont=1
                if cont0==0:
                    
                    b+=c
                    cont0=1
                
                if cont!=1:
                    b+=c       
    
    frase_listada=b.title()
    frase_listada1=frase_listada.strip()
    frase_listada2=frase_listada1.replace(" ",espacamento)
    
    return frase_listada2
