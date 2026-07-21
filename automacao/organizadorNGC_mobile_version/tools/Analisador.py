# função que analisa
import re

def analisador(teste):
    """
     essa função analisa um grupo de arquivos e agrupa em séries pelos seus nomes usando regex
     
     Padrões suportados:
        - Padrão 1: "Breaking Bad 5.mp4" (Nome + Espaço + Número)
        - Padrão 2: "Gachiakuta 1x2.mp4" (Nome + Temporada x Episódio)
        - Padrão 3: "Naruto S01E46.mp4" (Nome + SxxExx)

    Args:
        teste (list): Lista com os nomes dos arquivos de vídeo de origem.

    Returns:
        dict: Um dicionário onde a chave é o nome da série e o valor é
              uma lista com os episódios pertencentes a ela.

    """

    # padrao tipo> breaking bad 5.mp4
    padrao1 = re.compile(r"(.+)\s(\d+)(\.\w+)$")
    # padrao tipo> gachiakuta 1x2.mp4
    padrao2 = re.compile(r"(.+?)\s(\d+).+(\d+)(\.\w+)$")
    # padrao tipo> naruto S01E46.mp4
    padrao3 = re.compile(r"(.+)[sS](\d+)[eE](\d+)(\.\w+)$")

    series = {}

    # verificando os padroes das series
    for item in teste:
        match = re.search(padrao1, item)
        match2 = re.search(padrao2, item)
        match3 = re.search(padrao3, item)

        nome = None

        if match:
            nome = match.group(1).strip()
        elif match2:
            nome = match2.group(1).strip()
        elif match3:
            nome = match3.group(1).strip()

        if nome:
            # Aloca a memória e insere o arquivo na lista da série correspondente
            series.setdefault(nome, []).append(item)

    return series
