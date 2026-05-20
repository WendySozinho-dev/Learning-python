#cambio entre  moedas
moedas=[[],[],[]]#posicao 0 para o nome da moeda, 1 para o valor em dolar, 2 para conversao de 1 dolar para a moeda
comandos=("adicionar moedas","remover moedas", "consultar cambio","consultar comandos","comparar moedas")
contador=0
comparador1=0
comparador2=0
while True:
    #entrada de dados
    print("__"*15)
    entrada=input("comando de entrada:  ")
    if entrada == comandos[0]:
        print("~~"*15)
        lim=int(input("quantas moedas vais adicionar? "))
        for c in range(0,lim):
            print("~~"*15)
            moeda=(input(f"adicione a {c+1} moeda  "))
           #verificacao de moedas duplicadas
            while True:
                for c in moedas[0]:
                     if moeda == c:
                        print("xx"*15)
                        moedas=input("moeda existente tente outra  ")
                break
            print("--"*15)
            valor=float(input("quanto vale um dolar nessa moeda  "))
            # adicao das moedas e os valores a lista
            moedas[0].append(moeda)
            moedas[2].append(valor)
            trans=(1/valor)
            moedas[1].append(trans)
           # operacao de consulta
    if entrada == comandos[2]:
        print("~~"*15)
        consulta_m=input("que moeda deseja consultar?  ")
        for c in moedas[0]:
              if c == consulta_m:
                 pint(".,"*15)
                 print(f"1{c} custa {moedas[1][contador]} dolares")
        contador+=1
    #operacao de comparacao de moedas
    if entrada == comandos[4] and len(moedas[0]) >= 2 :
        print("~~"*15)
        print(f"temos as seguintes moedas digitadadas {moedas[0]}")
        moeda_c1=input("digite a moeda para comparar   ")
        while moeda_c1 not in moedas[0]:
            print("xx"*15)
            print("tal moeda nao foi digitada ")
            moeda_c1=input("digite novamente   ")
        print("--"*15)
        moeda_c2=input("digite a segunda moeda a comparar   ")
        while moeda_c2 not in moedas[0]:
           print("xx"*15)
           print("tal moeda nao foi digitada ")
           moeda_c2=input("digite novamente   ")
        contador=0
        #problema
        for c in moedas[0]:
               if moeda_c1==c:
                   comparador1=(moedas[1][contador])
               if moeda_c2==c:
                   comparador2=(moedas[1][contador])
               contador+=1  
               print(contador)
        resultado=(comparador1 - comparador2)
        if comparador1 > comparador2:
            print(".-"*15)
            print(f"{moeda_c1} e a mais pesada com {resultado} dolares de diferenca")    
        elif comparador1 < comparador2:
            print(".-"*15)
            print(f"{moeda_c2} e a mais pesada com {resultado} dolares de diferenca")
        else:
            print(".-"*15)
            print("perante o dolar, ambas tem o memo peso")
    elif entrada == comandos[4] and len(moedas[0]) < 2 :
        print("xx"*15)
        print("moedas insuficientes")



