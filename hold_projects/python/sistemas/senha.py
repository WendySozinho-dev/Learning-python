#senha de enyrada

senha=""
    
with open("senha.txt",'a') as f:
    pass
        
with open("senha.txt","r") as f:
        
        for c in f.read():
            senha=c        
        print(senha)
    
if senha=="":
    with open("senha.txt","w") as senha:
        entrada=input("digite a senha de bloqueio\na senha deve conter 8 caracteres\n")
        while len(entrada)<8:
            entrada=input("\033[32mdigite a senha de bloqueio\na senha deve conter 8 caracteres\033[m\n")

        senha.write(entrada)            
        




