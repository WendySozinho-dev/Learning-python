#exercicio 104
def leiaint(n):
    try:
        n1=float(n)
        return f"{n1} e um numero"
    except:
        return f"{n} nao e um numero"
        
        
        
n=leiaint("2e")
print(n)
#try-except servem para tentar executar um comando se der erro, sera executar o que estiver no except
