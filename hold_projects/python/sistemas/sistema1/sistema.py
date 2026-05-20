from ferramentas import*
from dados.gerenciador import*
from time import sleep

comandos=("sair do sistema","adicionar alguem na lista","mostrar pessoas cadastradas","remover algem da lista","calcular a media do peso","calcular a media de idade")

pessoas=()
nome=""
idade=0
peso=0
sexo=""
lista_de_pessoas=[]

while True:
    menu(comandos,"sistema")#responsavel por imprimir um menu
    conteudo=input("digite o comando\n")
    entrada=leiaint(conteudo)#responsavel por garantir que o usuario ira digitar um numero inteiro
    confirmacao=existe(entrada,comandos)#retorna True se o numero digitado estiver em len(comandos)
    while not confirmacao:#caso retorne falso tudo se repetira
        escreva("erro comando inexistente tente novamente")
        conteudo=input()
        entrada=leiaint(conteudo)
        confirmacao=existe(entrada,comandos)

#trabalhando com as escolhas do usuario
    if entrada==1:
        fecho="ate mais"
        print("\033[32m",end="")
        for c in fecho:
            print(c,end="",flush=True)
            sleep(0.4)
        break
           
    elif entrada==2:# resolvendo o caso do cadastro
        continuacao="s"
        while continuacao not in ("n","N"):
            nome=input("qual é o nome\n")#aqui o usuário digita o nome 
                        
            conteudo=input("qual é a idade\n")#aqui o usuário digita a idade
            idade=leiaint(conteudo)
                         
            conteudo=input("qual é o peso\n")#aqui o usuário digita o peso
            peso=leiareal(conteudo)
                                    
            sexo1=input("qual é o sexo\n")#aqui e a parte do sexo
            sexo2=sexo1.strip()
            sexo=sexo2.upper()
            if sexo=="M" or sexo=="F":
                sexo.strip()
                
            else:
                while not(sexo=="M"  or sexo=="F"):
                    sexo1=input("tente novamente\n")
                    sexo=sexo1.upper()       
                sexo.strip()
                  #fim da analize do sexo
                        
            #aqui vamos armazenar os dados recolhidos
            nome1=organizar(nome,"-")#responsavel por remover ps espacos desnecessarios e substituir por"-" 
            armazenar(nome1)
            armazenar(idade)
            armazenar(sexo)
            armazenar(f"{peso}\n")            
            escreva("sucesso")
            continuacao=input("quer continuar? [s/n]\n")
        
    elif entrada==3:#aqui mostramos o cadastro        
        mostrar_cadastro()
        sleep(2)        

    elif entrada==4:#tratando a 4a opcao
        nome1=input("digite o nome\n")
        nome=organizar(nome1)
        sobrescrever(nome)

    elif entrada==5:#trabalha a 5a opcao
        pessoas=cadastro()#lista de pessoas 
        print(pessoas[3])
        pesos=0
        cont=0
        cont1=0                
        escreva("eis os pesos")
        for c in pessoas[3::4]:
            print(c)
            numero=float(c)
            pesos+=numero
            cont+=1
        #trabalhando na identificacao da entidade mais pesada e a mais leve
        
            if float(peso)<float(c):
                nome=pessoas[cont1]
                idade=pessoas[cont1+1]
                sexo=pessoas[cont1+2]
                peso=pessoas[cont1+3]
            cont1+=4
                           
        media_peso=pesos/cont
        escreva(f"a media de peso e de {media_peso}")
        escreva(f"a pessoa mais pesada e {nome}, sexo {sexo}, com {idade} anos e pesando {peso}kg")

        peso=pessoas[3]
        cont1=0        
        for c in pessoas[3::4]:
            if float(peso)>float(c):
                peso=c
                nome=pessoas[cont1]
                idade=pessoas[cont1+1]
                sexo=pessoas[cont1+2]
                peso=pessoas[cont1+3]
            cont1+=4            
        escreva(f"a pessoa mais leve e {nome}, sexo {sexo}, com {idade} anos e pesando {peso}kg")

    elif entrada==6:#trabalhando a opcao 6
        pessoas=cadastro()#lista de pessoas 
        print(pessoas[1])
        idades=0
        cont=0
        cont1=0
        media_idade=0                
        escreva("eis as idades")
        for c in pessoas[1::4]:
            print(c)
            numero=float(c)
            idades+=numero
            cont+=1
        #trabalhando na identificacao da entidade mais velha e a mais nova
        
            if int(idade)<int(c):                
                nome=pessoas[cont1]
                idade=pessoas[cont1+1]
                sexo=pessoas[cont1+2]
                peso=pessoas[cont1+3]
            cont1+=4
                           
        media_idade=idades/cont
        escreva(f"a media de idade e de {media_idade} anos")
        sleep(2.4)
        escreva(f"a pessoa mais velha e {nome}, sexo {sexo}, com {idade} anos e pesando {peso}kg")
        sleep(2.4)
        
        idade=pessoas[1]
        cont1=0        
        for c in pessoas[1::4]:
            if int(idade)>float(c):                
                nome=pessoas[cont1]
                idade=pessoas[cont1+1]
                sexo=pessoas[cont1+2]
                peso=pessoas[cont1+3]
            cont1+=4            
        escreva(f"a pessoa mais nova e {nome}, sexo {sexo}, com {idade} anos e pesando {peso}kg")
        sleep(2.6)
