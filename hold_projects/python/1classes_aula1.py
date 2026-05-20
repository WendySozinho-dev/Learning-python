#classes
class pessoa:
    def __init__(self,altura,idade,nome,correndo=False,comendo=False):
        self.idade=idade
        self.altura=altura
        self.nome=nome
        self.correndo=correndo
        self.comendo=comendo
    

    def correr(self):
        if self.comendo:
            print(f"{self.nome} esta comendo no momento")
            return
        if self.correndo:
            print(f"{self.nome} esta a correr no momento")
        else:
            print(f"{self.nome} comecou a correr")
            self.correndo=True
            

    def comer(self):
        if self.correndo:
            print(f"{self.nome} nao pode correr comendo")
            return
        if self.comendo:
            print(f"{self.nome} ja esta comendo")
        else:
            print(f"{self.nome} comecou a comer")
            self.comendo=True



p1=pessoa(1.5,18,"wendy")
p1.comer()
p1.correr()
p1.comer()



