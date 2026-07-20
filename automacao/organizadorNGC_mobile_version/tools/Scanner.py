import re
def scanner(standard_text,files):
    """
    função de escaeamento que permite escanear uma lista de devolver
    outra lista com o conteudo filtrado
    
    args:
        standard_text(str); testo padrao que vai servir de filtro na lista
        files(list); a lista que queremos passar a vassoura

    rrturns:
        list; a lista que foi filtrada
    """

    
    # removendo caracteres que o regex usa
    correct_text = re.escape(standard_text)
    # defintndo o padrao
    standard = re.compile(f"{correct_text}")

    match = ""
    files_found = []
    # iniciando um loop para vreificar as sequencias
    for file in files:
        match = standard.findall(file)
        if match:
            files_found.append(file)
    return files_found
