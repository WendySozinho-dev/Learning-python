from ferramentas import*
comandos=("sair","registrar","ver lista")
while True:
    menu(comandos)
    entrada=leiaint(input("digite o comando\n"))
    confirmacao=existe(entrada,comandos)
    while not confirmacao:
        entrada=leiaint(input("tente novamente\n"))
        confirmacao=existe(entrada,comandos)
    
    if entrada==1:
        break
        
    elif entrada==2:
        with open("arquivo.txt","a") as file:
            while True:
                entrada=organizar(input("digite para ser organizado[--] para encerrar\n"))
                if entrada!="--":
                    file.write(f"{entrada} \n")
                else:
                    break
    
    elif entrada==3:
        try:
            with open("arquivo.txt","r") as file:
                conteudo=file.read().split()
                menu(conteudo)
        except:
            escreva("ocoreu um erro na leitura do arquivo")





