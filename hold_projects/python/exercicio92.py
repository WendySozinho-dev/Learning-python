#exercicio 92
from datetime import datetime
dados={}
dados["nome"]=str(input("nome  "))
ano_de_nascimento=int(input("ano de nascimento   "))
dados["idade"]=datetime.now().year-ano_de_nascimento
dados["carteira_de_trabalho"]=int(input("carteira de trabalho 0 nao tem  "))
if dados["carteira_de_trabalho"] != 0:
    dados["ano_de_contratacao"]=int(input("ano de contratacao  "))
    dados["salario"]=float(input("salario  "))
    dados["aposentadoria"]=(dados["idade"]+35),"anos" 
print("--"*20)
for k,v in dados.items():
    print(f"{k} tem valor {v}")
print("__"*20)
