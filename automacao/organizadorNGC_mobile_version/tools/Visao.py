# ==========================================================
# A VISÃO: SÓ VE E RETORNA (NÃO QUESTIONA O UTILIZADOR)
# ==========================================================
def visao(caminho):
    """
    Escaneia um diretório e retorna o seu conteúdo bruto.

    Esta função apenas lê o conteúdo da pasta informada, sem interagir
    com o usuário ou tomar decisões. É a camada de leitura pura do autômato.

    Args:
        caminho (str): O caminho absoluto do diretório que será escaneado.

    Returns:
        list: Uma lista de strings com os nomes dos arquivos e pastas encontrados.
        bool: Retorna False caso o diretório não exista ou não seja uma pasta.
    """


    if os.path.exists(caminho) and os.path.isdir(caminho):
        conteudo_bruto = os.listdir(caminho)
        return conteudo_bruto
    else:
        return False
