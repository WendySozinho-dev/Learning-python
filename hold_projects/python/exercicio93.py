#exercicio93
dados={}
dados["nome"]=str(input("qual o nome do jogador  "))
dados["partidas"]=int(input(f"quantas partidas {dados["nome"]} jogou?   "))
cont=0
somatorio=0
for c in range(0,dados["partidas"]):
    golos=int(input(f"quantos gols teve {dados["nome"]} na {cont+1} partida "))
    somatorio+=golos
    dados[f"golos{cont}"]=golos
    cont+=1
print("--"*15)
print(f"o somatorio total foi de {somatorio} golos")
cont=0
print("=-"*15)
for c in range(0,dados["partidas"]):
    print(f"na {cont+1} partida {dados["nome"]} teve",dados[f"golos{cont}"],"golos")
    cont+=1
