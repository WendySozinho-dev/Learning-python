def leiaint():
    valor=""
    num=0
    while True:
        try:
            valor=input("digite um numero inteiro   ")
            num=int(valor)
            print(f"vc digitou o numero {num}")
            break
        except:
            print(f"<{valor}> nao e um numero inteiro")
            

def leiafloat():
    valor=""
    num=0
    while True:
        try:
            valor=input("digite um numero real   ")
            num=float(valor)
            print(f"vc dgitou o numero {num}")
            break
        except:
            print(f"<{valor}> nao e um numero real")



leiaint()
leiafloat()