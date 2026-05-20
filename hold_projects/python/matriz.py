list=[[int(input("digite um valor ")),int(input("digite um valor ")),int(input("digite um valor ")) ],[int(input("digite um valor ")),int(input("digite um valor ")) ,int(input("digite um valor "))],[int(input("digite um valor ")),int(input("digite um valor ")),int(input("digite um valor "))]]
soma=0
soma2=0
for c in list:
    print(f"{c}")
for c in list: 
    for num in c:
        if num%2==0:
            soma+=num
for c in list[2]:
        soma2+=c
list[1].sort()
print(f"a soma dor numeros pares e {soma}")
print(f"a soma da terceira linha e {soma2}")
print(f"o maior valor da segunda limha e {list[1][-1]} ")
