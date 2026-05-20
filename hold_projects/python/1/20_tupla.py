#um programa de tuplas
print("digite um numero maior/menor que vinte/zero para parar o programa")
numeros=("zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","desasseis","desassete","dezoito","desanove","vinte" )
#
ent=int(input("digite um numero   "))
#
while ent <=20 and ent >=0 :
       print("vc digitou {} que e {} ".format(ent,numeros[ent] ))
       ent=int(input(" "))
       if ent >=21 or ent <=-1 :
           print("ate mais")
