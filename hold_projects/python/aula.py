#a variavel ent deve ser diferente de zero para que a condicao seja verdadeira e repita infinitamente, por isso que temos o ent=(1) no inicio do codigo, se colocasse [0] ao inves de um numero aleatorio, a proposocao se tornaria falsa e o laco nao ia ser considerada

ent=(1)#ent recebe (1)
while ent !=(0):# quando ent for diferente de 0
    ent=int(input("digite "))
    print(ent)
print(ent+1)
#isso serve para varias condicoes 
#para intender melhor essa parte recomendo que estude a logica matematica para seu bem   