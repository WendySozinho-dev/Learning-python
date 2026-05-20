#algoritmo que gera uma progressao aritmetica usando estructura de repeticao for
from time import sleep
print("o programa suporta números inteiros e estou com preguiça de mudar o código 😁 ")
x=int(input("digite o inicio da progressao aritmetica  "))
y=int(input("digite o fim da progressao aritmetica  "))
z=int(input("digite a distancia "))
print(x)
for c in range(x, y, z):    
    print(c+z)
    
print("a distancia d,",z," é adicionada com o valor inicial ", x ,"e vai adicionando até o fim que voçê adicionou",y,"em outras palavras, é uma contagem que começa de",x,"até",y,"que vai de",z,"em",z," fim😁.")    