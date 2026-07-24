# criando uma função que vai nasculhar 
import re
def scanner(standard_text,files,scan_format = 'near'):
    """
    função de escaeamento que permite escanear uma lista de devolver
    outra lista com o conteudo filtrado
    
    args:
        standard_text(str); testo padrao que vai servir de filtro na lista
        files(list); a lista que queremos passar a vassoura
        scan_format: o tipo de varredura que queremos realizar
            scan_format = 'near': busca aproximada
            scan_format = 'literal': busca exata

    returns:
        list; a lista que foi filtrada
    """

    
    # removendo caracteres que o regex usa
    correct_text = re.escape(standard_text)
    # defintndo o padrao
    standard = re.compile(f"{correct_text}")

    match = ""
    files_found = []
    if scan_format == 'near':
        # iniciando um loop para vreificar as sequencias
        for file in files:
            match = standard.findall(file)
            if match:
                files_found.append(file)
        return files_found
    
    elif scan_format == 'literal':
        # iniciando um loop para vreificar as sequencias
        for file in files:
            match = standard.match(file)
            if match:
                files_found.append(file)
        return files_found
