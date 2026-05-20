#segundo script de fisica
#tema lancamento horizontal
print("quais das formulas queres usar?")
print("{1} v(t)=v0 + gt: {2} y(t)=y0 +v0t + 1/2gt^(2): {3} a formula 2 mas para calcular a variacao do tempo")
ent=int(input("digite o numero da formula  "))
#comecando com a primeira formula
if ent==(1):
    for a in range(1,2):
        v01=float(input("qual e a velocidade inicial(m/s)  "))
        g1=float(input("qual e a gravidade (m/s^2) "))
        t1=float(input("qual e o tempo(s)  "))
        vt1=(v01 + g1 * t1 )
        print("a velocidade e",vt1,"m/s")
# agora vamos para a segunda formula
#os numeros que aparecem no fim das variaveis e consoante a alternativa escolhida
elif ent==(2):
     for a in range(1,2):
         y02=float(input("posicao inicial y0   "))
         t2=float(input("o tempo(t)  "))
         v02=float(input("a velocidade inicial(v0) "))
         g2=float(input("a gravidade(m/s*2)  "))
         yt2=(y02 + v02 * t2 +(g2 * t2 **(2))*1/2)
         print("o espaco em funcao do tempo e ",yt2,"m")   
#em caso de desacordo e melhor calcular por conta propria
#para auxilio nao para facilidade              