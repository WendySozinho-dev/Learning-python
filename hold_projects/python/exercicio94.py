#exercicio94
list=list()
dados={}
pessoas_acima_do_peso=[]
femeas=[]
numero_de_pessoas=0
while True:
    dados["nome"]=str(input("nome: "))
    dados["sexo"]=str(input("sexo:  "))
    while dados["sexo"].lower() !="m" and dados["sexo"].lower() != "f"   :
        del dados["sexo"]
        dados["sexo"]=str(input("erro digite novamente [m] para macho e [f] para femea "))
    dados["idade"]=int(input("idade:  "))
    list.append(dados)
    dados={}
    numero_de_pessoas+=1
    cont=str(input("quer continuar? [s/n]  "))
    while cont.lower() !="n" and cont.lower() != "s":
        cont=str(input("erro digite [s] para sim ou [n] para nao "))
    if cont.lower() =="n":
        break
print(f"foram cadastradas {numero_de_pessoas} pessoas")
idades=0
for c in list:
    idades+=c["idade"]
media=idades/numero_de_pessoas
print(f"a media foi e de {media} anos")
print(f"eis as mulheres cadastradas")
for c in list:
    if c["sexo"].lower()=="f":
        femeas.append(c)
        print(f" =>{c["nome"]} com {c["idade"]} anos")
for c in list:
    if c["idade"]>media:
       pessoas_acima_do_peso.append(c)
print("eis as pessoas acima do peso")
for c in pessoas_acima_do_peso:
      print(f"  =>{c["nome"]} de sexo {c["sexo"]} com {c["idade"]} anos")
