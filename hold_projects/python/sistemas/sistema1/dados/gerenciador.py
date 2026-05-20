from ferramentas import*
from time import sleep


def armazenar(lista):#responsavel por armazenar dados
    with open("dados/database.txt","a") as data:
        conteudo=str(lista)
        
        data.write(f"{conteudo} ")
    

def mostrar_cadastro():#responsavel por mostrar o cadastro
    nome=""
    idade=""
    peso=""
    sexo=""
    pessoas=[]
    cont=0
    
    try:
        with open("dados/database.txt","r") as data:
            pass   
    except:
        print("erro a criar um novo arquivo")
        
        with open("dados/database.txt","a") as data:
            pass
    else:
        with open("dados/database.txt","r") as data:
            print("eis as pessoas cadastradas")
            conteudo=data.read()
            
            conteudo1=conteudo.split()
            for a in range(0,len(conteudo1)):
                nome=conteudo1[cont].replace("-"," ")
                pessoas.append(nome)
                cont+=1
                
                idade=conteudo1[cont]
                pessoas.append(idade)
                cont+=1
                sexo=conteudo1[cont]
                pessoas.append(sexo)
                cont+=1
                peso=conteudo1[cont]
                pessoas.append(peso)
                cont+=1
                
                if cont>=len(conteudo1):
                    break
            menu(pessoas,cabecalho="lista",contador=("nome","idade","sexo","peso"),espaco="_____")                    
            
            
            
def remover_pessoas():
    nome=""
    idade=""
    peso=""
    sexo=""
    pessoas=[]
    cont=0
    
    try:
        with open("dados/database.txt","r") as data:
            pass   
    except:
        print("erro a criar um novo arquivo")
        
        with open("dados/database.txt","a") as data:
            pass
    else:
        with open("dados/database.txt","r") as data:
            print("eis as pessoas cadastradas")
            conteudo=data.read()
            
            conteudo1=conteudo.split()
            for a in range(0,len(conteudo1)):
                nome=conteudo1[cont].replace("-"," ")
                pessoas.append(nome)
                cont+=1
                
                idade=conteudo1[cont]
                pessoas.append(idade)
                cont+=1
                sexo=conteudo1[cont]
                pessoas.append(sexo)
                cont+=1
                peso=conteudo1[cont]
                pessoas.append(peso)
                cont+=1
                
                if cont>=len(conteudo1):
                    break
                cont=0
            menu(pessoas,cabecalho="lista",contador=("nome","idade","sexo","peso"),espaco="_____")
            return pessoas                    


def sobrescrever(lista):#responsavel por sobrescrever os dados no arquivo txt
    confirmacao=""
    cont=0
    cont1=0
    arquivo=()
    arquivo1=()
    item=0
    with open("dados/database.txt","r") as f:
        
        arquivo1=f.read()
        arquivo=arquivo1.split()
        
        
        for c in arquivo[::4]:
            if c==lista:
                confirmacao=input(f"quer remover {c}? [s/n]\n")
                if confirmacao=="s" or confirmacao=="S":
                    
                    del arquivo[cont:cont+4]
                    
                    print(f"{c} deletado")
                    
                    cont1=1
                   
            cont+=4
    sleep(0.2)
    if cont1==0:
        sleep(0.3)
        escreva("entidade nao encontrada")  
        sleep(0.5)      
    with open("dados/database.txt","w") as data:
        
        for c in arquivo:
            data.write(f"{c} ")
        

def cadastro():
        dados1=()
        dados=()
        try:
            with open("dados/database.txt","r") as f:
                   dados1=f.read()
                   dados=dados1.split()
                     
        except:
            print("erro")

        return dados
