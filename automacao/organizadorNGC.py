teste = ("naruto ultimate 1x1.mp4",
         "naruto ultimate 1x2.mp4",
         "naruto ultimate 1x3.mp4",
         "naruto ultimate 1x4.mp4",
         "naruto ultimate 1x5.mp4",
         "gachiakuta ep1.mp4",
         "gachiakuta ep2.mp4",
         "gachiakuta ep3.mp4",
         "gachiakuta ep4.mp4",
         "gachiakuta ep5.mp4",
         )
lista_animes = []
conjunto_numero_episodio = []

# primeiro, vamos detectar a terminacao e o episodio

for episodio in teste:
    terminacao = str("")
    numero_episodio = int()
    # pegando a terminacao do arquivo
    for letra in episodio[-1::-1]:
        if letra == ".":
            terminacao += letra
            break
        else:
            terminacao += letra
    print(terminacao)
    # pegando o numero do episodio
    for letra in episodio[len(terminacao)*-1::-1]:
        try:
            numero_episodio = int(letra)

        except ValueError:
            break

        else:
            conjunto_numero_episodio.append(numero_episodio)
        print(conjunto_numero_episodio)
