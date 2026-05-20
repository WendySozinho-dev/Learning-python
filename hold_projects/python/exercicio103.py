#exrecicio103
def ficha(nome="desconhecido",gols=0 ):
    if gols>0:
        return f"{nome} fez {gols} golos"
    else:
        return f"{nome} fez nenhum golo"


nome=str(input("nome  "))
gols=(int(input("gols  "))) 
ficha(nome,gols)
pessoa=ficha(nome,gols)
print(pessoa)
ficha()
pessoa=ficha()
print(pessoa)
