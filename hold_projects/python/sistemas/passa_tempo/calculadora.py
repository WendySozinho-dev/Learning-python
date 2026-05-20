#uma simples calculadora
from ferramentas import*

comandos=("clear","+","-","x","/")
escreva("uma simples calculadora")
valor_total=0
while True:
    conteudo=input("insira o valor\n")
    if conteudo==comandos[0]:
        valor_total=0
        conteudo="0"
        escreva("valor resetado")
    elif conteudo==comandos[1]:
        valor1=input("digite o valor a somar\n")
        valor2=leiareal(valor1)
        
        valor_momentaneo=valor+valor2
        valor_total+=valor_momentaneo
        escreva(f"a soma  momentania da {valor_momentaneo} ") 
        escreva(f"o valor tota dal {valor_total}")
        conteudo="0"
    
    elif conteudo==comandos[2]:
        valor1=input("digite o valor a somar\n")
        valor2=leiareal(valor1)
        
        valor_momentaneo=valor-valor2
        valor_total+=valor_momentaneo
        escreva(f"a subtracao momentania da {valor_momentaneo} ")
        escreva(f"o valor total da {valor_total}")
        conteudo="0"
    elif conteudo==comandos[3]:
        valor1=input("digite o valor a multiplicar\n")
        valor2=leiareal(valor1)
        
        valor_momentaneo=valor*valor2
        valor_total+=valor_momentaneo
        escreva(f"a multiplicacao momentania da {valor_momentaneo}")
        escreva(f"o valor total da {valor_total}")
        conteudo="0"
    elif conteudo==comandos[3]:
        valor1=input("digite o valor a divifir\n")
        valor2=leiareal(valor1)
        
        valor_momentaneo=valor/valor2
        valor_total+=valor_momentaneo
        escreva(f"a divisao momentania da {valor_momentaneo} ")
        escreva(f"o valor total da {valor_total}")
        conteudo="0"
    
    valor=leiareal(conteudo)
