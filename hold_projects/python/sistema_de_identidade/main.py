def menu(lista,cabecalho="menu",contador=(0),espaco=""):#responsavel por criar um simples menu e so tem um parametro obrigatorio
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
        
        
def linha(param=30,linha="_"):#responsavel por imprimir uma linha simples
    cont=""
    for c in range(0,param):
        print(linha,end="")
        cont+=linha
    print()
    return cont


def leiaint(valor):#responsavel por ler um numero inteiro e retorna esse valor
    num=0
    while True:
        try:
            num=int(valor)
        except:
            print(f"{valor} nao e um numero inteiro")
            valor=str(input("tente novamente\n"))
        else:
            return num

def existe(item,lista):#confirma se o item, que e um numero inteiro, se esta entre len(lista)
    valor=leiaint(item)
    caixa=len(lista)
    if valor>0 and valor<=caixa:
        return True
    else:
        return False


def escreva(txt):#responsavel por imprimir algo na tela de forma mais estilosa
    cont=0
    for c in txt:
       cont+=1 
    linha(cont,"-")
    print(f"\033[33m{txt}\033[m")
    linha(cont)
    

def leiareal(valor):#responsavel por ler um numero flutuante r retorna o numero
    num=0
    while True:
        try:
            num=float(valor)
        except:
            print(f"{valor} nao e um numero real")
            valor=str(input("tente novamente\n"))
        else:
            return num    

def sexo(sexo):#esqueca isso e so um rascunho
    if sexo=="M" or sexo=="m" or sexo=="F" or sexo=="f":
        escreva("sucesso")
        return sexo
    else:
        while not(sexo=="M" or sexo=="m" or sexo=="F" or sexo=="f"):
            sexo=input("tente novamente\n")
            

def organizar(txt,espacamento="-"):#responsavel por organizar uma fraze tirando os espacos inuteis 

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
    
















