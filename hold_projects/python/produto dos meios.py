#produtos dos meios e dos extremos
while True:
    var=input("qual e o nome da variavel  ")
    comp=input(f"queremos comparar {var} com?  ")
    x=float(input(f"quantos  {var} a comparar?  "))
    comparador=float(input(f"{x} {var} esta para quantos  {comp}?   "))
    comparador2=float(input(f"e quantos {comp} a comparar com {var}  "))
    x2=(x*comparador2)/comparador
    print("-="*13)
    print(f"deu {x2} {var}")
    cont=input("quer continuar? s/n ")
    while cont not in "sSnN":
         print("xx"*13)
         cont=input("nao entendi s para sim e n para nao  ")
    if cont in "nN":
        break
