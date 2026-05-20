#vamos testar a resoluvao do exercicio
numeros=(int(input("digite um numero ")),int(input("digite outro numero ")),int(input("digite mais um numero ")),int(input("digite o ultimo numero ")) )
#input pronto
print("o numero 9 apareceu {} veses".format(numeros.count(9)))
#numero 9 pronto
if 3 in numeros:
      print("o numero 3 apareceu na posicao {}".format(numeros.index(3)+1))
else:
    print("o numero 3 nao existe")
#    numero 3 pronto
print("eis os numeros pares")
for n in numeros:
    if n % 2 ==0:
        print(n, end=', ')
