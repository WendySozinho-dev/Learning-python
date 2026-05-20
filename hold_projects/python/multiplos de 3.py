#um algoritmo que mosrta multiplos de 3 de 1 ate o limite que o usuario desejar usando a estructura de repeiçao {for}
from time import sleep 
print("esse algoritmo mostra os multiplos de 3 perfeitos") 
f=int(input("digite o fim do agoritmo  "))
for c in range(3, f, 3):
    sleep(0.2)
    print(c) 
