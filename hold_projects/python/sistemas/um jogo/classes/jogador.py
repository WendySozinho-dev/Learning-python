from random import*

class jogador:
    def __init__(self,nome="player"):
        self.nome=nome
        self.hp=10
        self.defesa=2
        self.nivel=1
        self.xp=float(0.0)
        self.dano=6
        
        
    
    def dano(self,dano):
        dano_real=dano-self.defesa
        if dano_real<0:
            dano_real=0
        self.hp-=dano_real
        
        
    def subir_de_nivel(self,xp):
        xp_necessario=self.nivel*50
        self.xp+=xp
        if self.xp>=xp_necessario:
            self.nivel+=1
            print(self.nivel)
    
    
    def atacar(self):
       ataque=randint(self.dano-3,self.dano+3)
       if ataque<=0:
           ataque=1
       return ataque
        
    
        