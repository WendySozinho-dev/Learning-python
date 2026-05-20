from ferramentas import *

while True:
    item=0
    item2=0
    contador=0.0
    contador2=0.0
    sub_contador=0.0
    sub_contador2=0.0
    for c in range(0,5):
       item=input(f"\no {c+1} valor\n")
       
       if item=="--":
           sub_contador=0
           while True:
               item=input("\033[32mdigite o valor ")
               if item=="--" and sub_contador>0:
                   print("\033[m")
                   break
               
               elif item=="--" and sub_contador==0:
                   item=leiareal(input("\033[mdigite o valor\n"))
                   sub_contador=item
                   break
               
               
               item2=leiareal(item)

               sub_contador+=item2
           item=sub_contador                  
       
       entrada=leiareal(item)
       contador+=entrada
         
    escreva(f"o primeiro teste foi {contador}")    
    
     
    for c in range(0,5):
       item=input(f"\no {c+1} valor\n")
       if item=="--":
           sub_contador=0
           while True:
               item=input("\033[32mdigite o valor ")
               if item=="--" and sub_contador2>0:
                   print("\033[m")
                   break
               
               elif item=="--" and sub_contador2==0:
                   item=leiareal(input("\033[mdigite o valor\n"))
                   sub_contador=item
                   break
                              
               item2=leiareal(item)

               sub_contador2+=item2
           item=sub_contador2
              
       entrada=leiareal(item)
       contador2+=entrada
    
    escreva(f"o primeiro teste foi {contador}\no segundo teste foi {contador2}")
    continuacao=input("continuar? enter ara continuar\n")
    if continuacao != "":
        break
        
     