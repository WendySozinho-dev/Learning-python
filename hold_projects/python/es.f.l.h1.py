#segundo script de fisica 
#tema: lancamento horizontal
#estructura de repetiçao while adicionada
cont=(1)
print("quais das formulas queres usar?")
print("{1} v(t)=v0 + gt: {2} y(t)=y0 +v0t + 1/2gt^(2): {3} a formula 2 mas para calcular a variacao do tempo"),

while cont==(1):
         ent=int(input("digite o numero da formula  "))       
         
#comecando com a primeira formula
         if ent==(1):
             for a in range(1,2):
                 v0_1=float(input("qual e a velocidade inicial(m/s)  "))
                 g_1=float(input("qual e a gravidade (m/s^2) "))
                 t_1=float(input("qual e o tempo(s)  "))
                 vt_1=(v0_1 + g_1 * t_1 )
                 print("a velocidade e",vt_1,"m/s")
# agora vamos para a segunda formula
#os numeros que aparece  no fim das variaveis e consoante a alternativa escolhida
         elif ent==(2):
              for a in range(1,2):
                   y0_2=float(input("posicao inicial y0   "))
                   t_2=float(input("o tempo(t)  "))
                   v0_2=float(input("a velocidade inicial(v0) "))
                   g_2=float(input("a gravidade(m/s^2)  "))
                   yt_2=(y0_2 + v0_2 * t_2 +(g_2 * t_2 **(2))*1/2)
                   print("o espaco em funcao do tempo e ",yt_2,"m")   
#em caso de desacordo e melhor calcular por conta propria
#para auxilio nao para facilidade 
#agora vamos para a formula 3
         elif ent ==(3):
              for a in range(1,2):
                    v0_3=float(input("qual e a velocidade inicial(m/s)  "))
                    g_3=float(input("qual e a gravidade(m/s^2)   "))
                    y0_3=float(input("qual e a posiçao inicial(m)   "))
                    t1_3=(v0_3 +(v0_3**(2) - 2*g_3*y0_3)**1/2)/g_3
                    t2_3=(v0_3 -(v0_3**(2) - 2*g_3*y0_3)**1/2)/g_3
                    vt1_3=(t1_3 - t2_3)
                    vt2_3=(t2_3 - t1_3)
                    print("o tempo1 e",t1_3,"e o tempo2 e",t2_3,"s") 
                    print("a variaçao de tempo e",vt1_3,"ou",vt2_3,"segundos")
                    
                      
#mais uma formula com sucesso
#agora vamos para a formula 4










         print("quer coninuar? {1}sim {2}nao")
         cont=int(input("DIGA   "))    