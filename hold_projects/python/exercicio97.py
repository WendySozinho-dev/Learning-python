#exercicio97
def escreva(txt):
    n_linha=0
    for c in txt:
         n_linha+=1
    print("~"*n_linha)
    print(txt)
    print("~"*n_linha)


escreva("ola mundo")
x=str(input("digite algo  "))
escreva(x)
