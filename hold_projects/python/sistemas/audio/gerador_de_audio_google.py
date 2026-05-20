# 1. Instalar a biblioteca: pip install gtts

# 2. Importar a classe
from gtts import gTTS
import os # Módulo para interagir com o sistema operacional (usado aqui para reproduzir o áudio)

# 3. Definir o texto e o idioma
texto = "Olá, este é um exemplo de conversão de texto para áudio com gTTS."
idioma = 'pt'

# 4. Criar o objeto gTTS
tts = gTTS(text=texto, lang=idioma, slow=False)

# 5. Salvar o arquivo de áudio
nome_arquivo = "meu_audio_gtts.mp3"
tts.save(nome_arquivo)

print(f"Áudio salvo como '{nome_arquivo}'")

# 6. (Opcional) Tocar o áudio (funciona em alguns ambientes como Jupyter Notebooks ou com o sistema operacional)
# Se estiver em um ambiente que não reproduz diretamente, você pode precisar abrir o arquivo no seu player de áudio.
# Para reproduzir no sistema operacional (em sistemas que suportam 'start' ou 'xdg-open'):
# os.system(f"start {nome_arquivo}") # No Windows
# os.system(f"xdg-open {nome_arquivo}") # No Linux
# os.system(f"open {nome_arquivo}") # No macOS