# algoritmo para calcular uma tabuada
from time import sleep
n=int(input("digite um numero para ser multiplicado {um numero inteiro}   "))
x=int(input("inicio da tabuada {um numero inteiro} "))
z=int(input("fim da tabuada {um numero inteiro} "))
for a in range(x, z+1):
   print(a,"x",n,"=", a*n)    
#   sleep(0.2) 