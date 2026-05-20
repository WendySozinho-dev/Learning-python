#exercicio 101
from datetime import datetime
def voto(ano):
    idade=datetime.now().year-ano
    if idade < 18:
        return "nao da para vota"
    elif idade >=18 and idade <=64:
        return "voto obrigatorio"
    else:
        return "vc decide se vota ou nao"
        

idade=int(input("em qie ano nasceu?    "))
voto(idade)
for c in voto(idade):
    print(c, end="")
