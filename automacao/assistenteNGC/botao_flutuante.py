import sys
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QPushButton

class BotaoFlutuante(QPushButton):
    def __init__(self):
        super().__init__()
        
        # 1. Configurações do Botão Redondo (Tamanho 70x70)
        self.resize(70, 70)
        self.setText("🤖")
        
        # Estilização com CSS (Fundo vermelho, letra branca, borda redonda perfeita)
        self.setStyleSheet("""
            QPushButton {
                background-color: #ff1744;
                color: white;
                font-size: 24px;
                border-radius: 35px; /* Metade da largura/altura para ficar redondo */
                border: 2px solid white;
            }
            QPushButton:pressed {
                background-color: #b2102f; /* Muda de cor ao clicar */
            }
        """)

        # 2. Remover bordas da janela e torná-la transparente/sempre no topo
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # Posição inicial para arrastar
        self.antiga_posicao = QPoint()

    # --- Lógica de Arrastar o Botão com o Dedo/Mouse ---
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.antiga_posicao = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            delta = QPoint(event.globalPos() - self.antiga_posicao)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.antiga_posicao = event.globalPos()

    def mouseReleaseEvent(self, event):
        # Se o usuário clicou e não arrastou quase nada, conta como clique!
        if event.button() == Qt.LeftButton:
            self.acao_do_botao()

    def acao_do_botao(self):
        print("Botão PyQt5 clicado com sucesso!")
        # Coloque o seu script aqui dentro

if __name__ == "__main__":
    app = QApplication(sys.argv)
    botao = BotaoFlutuante()
    botao.show()
    sys.exit(app.exec_())

