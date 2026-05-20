from random import*

class inimigo:
    def __init__(self,nivel):
        self.hp=10*nivel
        self.defesa=3*nivel
        self.ataque=4*nivel
        
    
    def atacar(self):
        ataque=randint(self.ataque-3,self.ataque+4)
        return ataque
    
    
    def dano_inimigo(self,dano):
        dano_real=dano-self.defesa
        if dano_real<=0:
            dano_real=1
        self.hp-=dano_real
        print(f"reducao de dano {dano_real}")
    
    def vitalidade(self):
        return self.hp    
    
    
    
    
    
    
    