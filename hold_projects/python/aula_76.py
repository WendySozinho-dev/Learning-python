palavras=("joao","maria","apanhar","levar","agradecer","visitar","enriquecer","enloquecer")
for p in palavras:
    print("."*30)
  #  print(c,":  a vogal *a* aparece",c.count("a"),"veses","a vogal *e* aparece",c.count("e"),"veses","a vogal *i* aparece",c.count("i"),"veses","a vogal *o* aparece",c.count("o"),"veses","a vogal *u* aparece",c.count("u"),"veses")
    print("\n na palavra {} existe".format(p))  
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end="  ") 
             
    print("."*30)
        