import re


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
         "breaking bad 05.mp4",
         "atack on titan s1e3.mp4",
         )
lista_animes = []
# padrao tipo> breaking bad 5.mp4
padrao1 = r"(.+)\s(\d+)(\.\w+)"
# padrao tipo> gachiakuta 1x2.mp4
padrao2 = r"(.+?)\s(\d+).+(\d+)(\.\w+)"
# padrao tipo naruto S01E46.mp4
padrao3 = r"(.+)[sS](\d+)[eE](\d+)(\.\w)"

for item in teste:
    match = re.search(padrao1, item)
    match2 = re.search(padrao2, item)
    match3 = re.search(padrao3, item)

    if match:
        nome = match.group(1)
        episodio = match.group(2)
        extensao = match.group(3)

        print(f"nome: {nome}\nepisodio: {episodio}\nextensao: {extensao}")

    elif match2:
        nome = match2.group(1)
        temporada = match2.group(2)
        episodio = match2.group(3)
        extensao = match2.group(4)

        print(f"nome: {nome}\ntemporada: {temporada}\nepisodio: {episodio}\nextensao: {extensao}")

    elif match3:
        nome = match3.group(1)
        temporada = match3.group(2)
        episodio = match3.group(3)
        print(f"nome: {nome}\ntemporada: {temporada}\nepisodio: {episodio}")

