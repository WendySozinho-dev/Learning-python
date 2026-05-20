import random2
n1=(random2.randint(1,5))
n2=(random2.randint(1,5))
n3=(random2.randint(1,5))
n4=(random2.randint(1,5))
n5=(random2.randint(1,5))
#
numeros=(n1,n2,n3,n4,n5)
print("foram gerados {}, {}, {}, {}, {} numeros  ".format(numeros[0],numeros[1],numeros[2],numeros[3],numeros[4]))
#
for c in range(1,6):
    m=(c)
    if c==numeros[0] or c==numeros[1] or c==numeros[2] or c==numeros[3] or c==numeros[4] :
        break
print("o menor numero e {}".format(m))
#
for a in range(5,1,-1):
    n=(a)
    if a==numeros[1] or a==numeros[2] or a==numeros[3] or a==numeros[4]:
        break
print("o maior numero e {}".format(n))
