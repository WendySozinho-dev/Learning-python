from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse
from kivy.core.window import Window

class InterfaceFlutuante(FloatLayout):
    def __init__(self, **kwargs):
        # O super() garante que a classe base FloatLayout seja inicializada corretamente
        super(InterfaceFlutuante, self).__init__(**kwargs)
        
        # Define o tamanho padrão do nosso widget redondo (200x200 pixels)
        self.size_hint = (None, None)
        self.size = (200, 200)
        # Posiciona o elemento no centro da tela
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        
        # O canvas gerencia a renderização de formas geométricas no Kivy
        with self.canvas.before:
            # 1. Define a cor do círculo (R, G, B, A). 
            # R=0.2, G=0.6, B=1.0 (Azul) e A=0.7 (70% de opacidade/transparência)
            Color(0.2, 0.6, 1.0, 0.7)
            
            # 2. Desenha o círculo perfeito (Ellipse com largura e altura iguais)
            # pos=self.pos vincula a posição do círculo à posição do FloatLayout
            # size=self.size vincula o tamanho do círculo ao tamanho do FloatLayout
            self.circulo = Ellipse(pos=self.pos, size=self.size)
            
        # Garante que o desenho do círculo se mova/atualize caso o layout mude de posição
        self.bind(pos=self.atualizar_desenho, size=self.atualizar_desenho)
        
        # Criamos um botão simples para interagir dentro do círculo
        botao = Button(
            text="Fechar",
            size_hint=(None, None),
            size=(80, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}, # Centraliza o botão dentro do círculo
            background_color=(1, 0, 0, 0.8) # Botão vermelho semi-transparente
        )
        # Vincula o clique do botão à função de fechar o app
        botao.bind(on_press=self.fechar_app)
        self.add_widget(botao)

    def atualizar_desenho(self, *args):
        # Atualiza a posição e o tamanho da elipse quando o widget se move
        self.circulo.pos = self.pos
        self.circulo.size = self.size

    def fechar_app(self, instance):
        App.get_running_app().stop()

class AppRedondo(App):
    def build(self):
        # Remove a cor de fundo padrão da janela do Kivy (torna o fundo 100% transparente)
        Window.clearcolor = (0, 0, 0, 0)
        return InterfaceFlutuante()

if __name__ == '__main__':
    AppRedondo().run()

