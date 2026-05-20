from ferramentas import*
from dados.gerenciador import*
from time import sleep

comandos=("sair do sistema","adicionar uma nova tarrefa","mostrar tarrefas existentes","remover uma tarefa")
tarrefas=gerenciador
while True:
    
    menu(comandos,cabecalho="gerenciador de tarrefas")
    conteudo=input("digite o comando\n")
    entrada=leiaint(conteudo)
    confirmacao=existe(entrada,comandos)
    while not confirmacao:
        conteudo=input("digite o comando\n")
        entrada=leiaint(conteudo)
        confirmacao=existe(entrada,comandos)
    
    if entrada==1:
        fecho="ate mais"
        print("\033[32m",end="")
        for c in fecho:
            print(c,end="",flush=True)
            sleep(0.4)            
        break    
    
    elif entrada==2:
        conteudo=input("que tarefa desejas adicionar?\n")
        tarrefas.armazenar(conteudo)
        
    
    elif entrada==3:
        tarrefas.mostrar_tarrefas()    
    
    
    elif entrada==4:
        while True:
            lista_de_tarrefas=tarrefas.obter_tarrefas()
            menu(lista_de_tarrefas,cabecalho="eis as tarrefas")
            conteudo=input("que tarrefa deseja remover?\n")
            entrada=leiaint(conteudo)
            confirmacao=existe(entrada,lista_de_tarrefas)
            while not confirmacao:
                    conteudo=input("opcao inexistente tente novamente(^_^)\n")
                    entrada=leiaint(conteudo)
                    confirmacao=existe(entrada,lista_de_tarrefas)
            del lista_de_tarrefas[entrada-1]
            print(lista_de_tarrefas)
            tarrefas.sobrescrever(lista_de_tarrefas)
            continuidade=input("quer continuar?[s/n]\n")
            if not(continuidade=="s"or continuidade=="S"):
                break
    
    