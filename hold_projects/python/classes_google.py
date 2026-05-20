class MinhaClasse:
    atributo_classe = 0

    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia

    # Método de instância
    def metodo_instancia(self):
        print(f"Atributo de instância: {self.atributo_instancia}")
        print(f"Atributo de classe: {self.atributo_classe}")

    # Método de classe
    @classmethod
    def metodo_classe(cls):
        print(f"Atributo de classe: {cls.atributo_classe}")
        print(f"Classe: {cls.__name__}")