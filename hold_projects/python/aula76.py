print("eis os produtos e op seus precos")
print("-"*30)
produtos=("arroz/kg",60,"acucar/kg",80,"peixe/kg",100,"espargete",30,"feijao",40,"reffrigerante",50,"yogurte",30,"fosfoto",4,"lapiz",5,"borracha",4 )
for c in range (0, len(produtos)) :
      if c % 2 ==0:   
               print(produtos[c],"."*15,end=" ")
      else:
          print(produtos[c])

