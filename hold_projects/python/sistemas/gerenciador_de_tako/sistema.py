from ferramentas import*
from dados.gerenciador import*
from datetime import datetime


comandos=("sair do sistema","criar nova anotacao","consultar anotacoes","deletar anotacao")
consulta=("mostrar anotacoes","remover anotacoes","selecionar anotacao para manipular")

while True:
    menu(comandos,cabecalho="gerenciador")
    entrada=leiaint(input("digite o comando\n"))
    confirmacao=existe(entrada,comandos)
    while not confirmacao:
        entrada=leiaint(input("valor inexistente\n"))
        confirmacao=existe(entrada,comandos)
    
    if entrada==1:
        print("ate mais")
        break

    elif entrada==2:
        pessoas={}
        
        nome_da_nota=input("digite o nome da anotacao\n")
        valor=leiareal(input("digite o valor total\n"))
        numero_de_pessoas=leiaint(input("quantas pessoas participarao\n"))
        valor_dividido=valor/numero_de_pessoas
        lider=input("quem e o lider")
        pessoas[lider]=valor_dividido
        for c in range(0,pessoas-1):
            pessoa=input(f"nome da {c} pessoa\n")
        print(pessoas)            
            
            
            
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    elif entrada==3:
        notas=obter_anotacoes()
        while True:
            menu(consulta)
            entradda=leiaint(input("digite o comando\n"))
            
            
        
        
        






