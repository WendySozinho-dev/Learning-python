#exercicio102
def factorial(termo,show=False):
    list=[]
    num=termo-1
    multiplo=0
    if show:
        for c in range(termo,1,-1):
            multiplo+=c*num
            num-=1
            list.append(c)
            list.append("x")
        list.append("=")
        list.append(multiplo)
        return list 
            
    else:
        for c in range(termo,1,-1):
            multiplo+=c*num
            num-=1
        return multiplo        
        

        
oi=factorial(400,show=False)
print(oi)
