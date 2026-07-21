import os
from textual.containers import VerticalScroll
from textual.widgets import Button, Footer, Header, Static
from textual.app import App, ComposeResult
from textual import work
import subprocess

class explorerNGC(App[str]): # o [str] indica que o app retorna uma string
    
    BINDINGS = [("q", "quit", "sair")]

    def __init__(self):
        super().__init__()
        self.diretory = ""

    def compose(self) -> ComposeResult:
        # Header e Footer fixos aqui, renderizados apenas UMA vez
        yield Header()
        yield Static("📂 exploradorNGC", id="app_title")
        yield Static("Selecione a origem", id="current_path")
        
        with VerticalScroll(id="file_box"):
            android_root = "/storage/emulated/0"
            this_root = os.path.expanduser("~")

            if android_root != this_root:
                yield Button(android_root, id="android_root", classes="root")
                yield Button(this_root, id="this_root", classes="root")
            else:
                yield Button(this_root, id="this_root")
                
        yield Footer()

    # O decorador @work transforma a função em uma tarefa assíncrona em background,
    # impedindo que a interface trave enquanto lê o disco.
    @work(exclusive=True)
    async def update_list(self) -> None:
        box = self.query_one("#file_box", VerticalScroll)
        path_label = self.query_one("#current_path", Static)
        
        # Atualiza o texto do diretório atual de forma limpa
        path_label.update(f"📍 {self.diretory}")

        folders = []
        files = []

        # os.scandir é ordens de magnitude mais rápido que os.listdir + os.path.isdir
        try:
            with os.scandir(self.diretory) as it:
                for entry in it:
                    if entry.is_dir():
                        folders.append(entry.name)
                    else:
                        files.append(entry.name)
        except PermissionError:
            self.notify("Permissão negada!", severity="error")
            return

        folders.sort()
        files.sort()

        # Remove os botões antigos de uma vez só
        for hold_button in box.query(Button):
            hold_button.remove()

        # Lista para acumular os novos widgets na memória
        new_widgets = []
        
        # Botão de voltar
        new_widgets.append(Button("⬅️ Voltar", classes="system", variant="error"))

        # Botao para concluir
        new_widgets.append(Button("✅ concluir", classes = "system", variant="success"))
        
        # Cria os botões de pastas
        for item in folders:  
            new_widgets.append(Button(f"📁 {item}", classes="folder"))
                    
        # Cria os botões de arquivos
        for item in files:
            new_widgets.append(Button(f"📄 {item}", classes="file"))
        
        # Monta TUDO de uma única vez no container (Ganho massivo de performance)
        if new_widgets:
            box.mount_all(new_widgets)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        btn = event.button

        if "root" in str(btn.classes):
            if "android_root" in str(btn.id):
                self.diretory = "/storage/emulated/0"
            else:
                self.diretory = os.path.expanduser("~")
            self.update_list()
            
        elif "folder" in str(btn.classes):
            # Remove o emoji do início para pegar o nome puro da pasta
            folder_name = str(btn.label)[2:]
            self.diretory = os.path.join(self.diretory, folder_name)
            self.update_list()
            
        elif "file" in str(btn.classes):
            self.notify(f"Arquivo selecionado: {str(btn.label)[2:]}")
            
        elif "system" in str(btn.classes):
            if "Voltar" in str(btn.label):
                # Evita subir além da raiz do sistema
                parent = os.path.dirname(self.diretory)
                
                if parent != self.diretory:
                    self.diretory = parent
                    self.update_list()
            else:
                self.exit(str(self.diretory))









if __name__ == "__main__":
    # app = explorerNGC()
    # diretory=app.run()

    try:
        with open("ngc_init.txt","r") as file:
            diretory = file.read()
    except FileNotFoundError:
        app = explorerNGC()
        diretory = app.run()
        with open("ngc_init.txt","w") as file:
            file.write(diretory)


    

