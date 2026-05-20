from gtts import gTTS
txt=input("digite o texto\n")
nome=input("digite o nome do audio\n")+".mp3"
audio=gTTS(text=txt,lang="en",slow=True)
audio.save(nome)
print("done")