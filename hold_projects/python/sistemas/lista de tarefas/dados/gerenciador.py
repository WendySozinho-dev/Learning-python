from ferramentas import*
from time import sleep

class gerenciador:
    
    
    def __init__(self):
        #self.tarrefa=tarrefa
        #self.tempo_limite=tempo_limite
        pass
        
    def armazenar(tarrefa):
        with open("dados/database.txt","a") as file:                
                tarrefas=organizar(tarrefa)
                print(tarrefas)
                file.write(f"{tarrefas} \n")
                

    def mostrar_tarrefas():
        try:
            with open("dados/database.txt","r") as file:
                conteudo=file.read()
                tarrefas1=conteudo.split()
                conteudo=""
                tarrefas=[]
                for c in tarrefas1:
                    conteudo=c.replace("-"," ")
                    tarrefas.append(conteudo)
                sleep(1.5)
                menu(tarrefas,cabecalho="tarrefas programadas")
                sleep(1.5)
                
        except:
            escreva("erro")
            with open("dados/database.txt","a"):
                pass
            

    def obter_tarrefas():
        try:
            with open("dados/database.txt","r") as file:
                conteudo=file.read()
                tarrefas1=conteudo.split()
                conteudo=""
                tarrefas=[]
                for c in tarrefas1:
                    
                    tarrefas.append(c)
            return tarrefas
        except:
            with open("daos/database.txt","a"):
                pass
        
    def sobrescrever(lista):
            with open("dados/database.txt","w") as database:
                for c in lista:
                    database.write(f"{c} \n")