"""
crie um programa que você coloca muitas palavras
ou numeros, com base na percentagem, o programa deve 
saber qual é o próximo item que vem de seguida
por enquanto que seja de 4 em 4
"""

from random import choice
from time import sleep

def percentagem(dicionario):#esta funcao e responsavel por calcular a percentagem
    valor_maximo=len(dicionario)
    #print(f"valor maximo da percentagem {valor_maximo}\n")
    dicionario_de_percentagem={}
    
    for item,frequencia in dicionario.items():
        x=round(float((frequencia*100)/valor_maximo),2)
        dicionario_de_percentagem[item]=x
        
    #print(dicionario_de_percentagem)
    return dicionario_de_percentagem


def frequencia(lista):#esta funcao e responsavel por por detectar a frequencia que um item aparece na lista
    
    contador_de_item=1
    itens={}
    
    for c in lista:#criando os indices do dicionario
        if not c in itens:            
            itens[c]=contador_de_item
    for i in itens.keys():#inserindo o verdadeiro valor no dicionario
        contador_de_itens=lista.count(i)        
        itens[i]=contador_de_itens
        
    return itens    
        

padroes=[]
padrao1=[]
padrao2=[]
padrao3=[]
padrao4=[]

entrada=()
contador=0

while True:
    # entrada de dados 
    for c in range(1,5):
        entrada=input(f"digite o padrao [{c}]    ")
        padroes.append(entrada)
        
    entrada=input("deseja continuar? [s/n]    ")
    if entrada=="n":
        break


"""
reconhecimento de padrao nas posiçoes 0,3, etc...
baseado na chance de um item aparecer nas posiçoes 0,3,7,11,etc...
"""
#recolho o item do indice 0 de padroes
for item in padroes[::4]:
    padrao1.append(item)

for item in padroes[1::4]:#recolho o padrao do indice 1
    padrao2.append(item)

for item in padroes[3::4]:#recolho o padrao do indice 2
    padrao3.append(item)

for item in padroes[2::4]:#recolho o padrao do indice 3
    padrao4.append(item)


#aqui comeca a fase de adivinhar o proximo item
percentagens1=percentagem(frequencia(padrao1))
percentagens2=percentagem(frequencia(padrao2))
percentagens3=percentagem(frequencia(padrao3))
percentagens4=percentagem(frequencia(padrao4))
while True:
    
    item_chute=choice(padrao1)
    for item,chance in percentagens1.items():
        print(f"existe {chance}% de chanses de aparecer {item}\n\n")
        sleep(0.5)
    print(f"vou chutar <<{item_chute}>>")
    sleep(0.5)
    
    item_chute=choice(padrao2)
    for item,chance in percentagens2.items():
        print(f"existe {chance}% de chances de aparecer {item}\n\n")
        sleep(0.5)
    print(f"vou chutar <<{item_chute}>>")
    sleep(0.5)
    
    item_chute=choice(padrao3)
    for item,chance in percentagens3.items():
        print(f"existe {chance}% de chances de aparecer {item}\n\n")
        sleep(1)
    print(f"vou chutar <<{item_chute}>>")
    sleep(1)
    
    item_chute=choice(padrao4)
    for item,chance in percentagens4.items():
        print(f"existe {chance}% de chances de aparecer {item}\n\n")
        sleep(1)
    print(f"vou chutar <<{item_chute}>>")
    sleep(1)
    
    entrada=input("quer continuar? [s/n]    ")
    if entrada=="n":
        break
         