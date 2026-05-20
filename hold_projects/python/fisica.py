#algoritmo que ajuda na fisica
#tema: lancamento horizontal 
print("escolha uma formula")
print("{1}equacao da velocidade em funcao do tempo v(t)=v0 +  gt:")
print(" {2}equacao da posicao em funcao do tempo y(t)=y0 + v0t +1/2gt^(2):")
print(" {3}equacao da posicao em funcao da velocidade (equacao de torriceil) v^(2)=v0^(2)+2g∆y   ")
#calculando a velocidade em funcao do tempo
ent=int(input("digite o valor aqui  "))
#preciso de criar mais possibilidades de calculos
if ent ==1:
    for a in range(1,2):
        
        v0=float(input("digite a velocidade inicial  "))
        g=float(input("digite a gravidade  "))
        t=float(input("digite o tempo "))
        vt=(v0 + g*t)
        print("considerando a formula escolhida v(t)= v0 +gt: a velocidade em funcao do tempo e", vt,"m/s" )
#equacao da posicao em funcao do tempo        
elif ent==(2):
     for a in range(1,2):
         y0= float(input("digite o valor da posicao inicial(y0)  "))
         v0= float(input("digite a velocidade inicial(v0)  "))
         t=float(input("digite o tempo "))
         g= float(input("digite a gravidade "))
         yt=(y0+v0*t+(1/2*g*t**2))   
         print("a posicao em funcao tempo e",yt,"'m")   