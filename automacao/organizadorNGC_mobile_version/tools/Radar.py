import os

def radar(root):
    # Lista global onde vamos guardar as coordenadas finais de cada arquivo
    todos_os_arquivos = []

    # O os.walk vai iterar pasta por pasta automaticamente
    for pasta_atual, subpastas, arquivos in os.walk(root):
        
        # Para cada arquivo solto encontrado na pasta atual:
        for arquivo in arquivos:
            # Funde o caminho da pasta atual com o nome do arquivo
            caminho_completo = os.path.join(pasta_atual, arquivo)
            
            # Adiciona à nossa lista de alvos
            todos_os_arquivos.append(caminho_completo)

    return todos_os_arquivos

