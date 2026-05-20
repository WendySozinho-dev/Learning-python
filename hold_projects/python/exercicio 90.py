#exercicio 90
pauta={}
pauta["nome"]=str(input("nome do aluno  "))
pauta["media"]=float(input(f"media de {pauta["nome"]}  "))
print(f"{pauta["nome"]} teve {pauta["media"]}")
if pauta["media"] <9.5:
    print("chumbou")
else:
    print("passou")
