from ferramentas import*

def obter_anotacoes():
    try:
        with open("dados/anotacoes.txt","r") as file:
            pass
            
    except:
        print("arquivo inexistente")
        print("gerando o arquivo")
        with open("dados/anotacoes.txt","w"):
            pass
    
    else:
        with open("dados/anotacoes.txt","r") as file:
            notas=file.read()
            return notas
