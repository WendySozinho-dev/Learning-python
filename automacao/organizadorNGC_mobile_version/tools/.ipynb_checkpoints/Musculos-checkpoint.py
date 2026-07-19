# a função que move os arquivos

#====================================================================
# OS MUSCULOS: ENCARREGADOS DE MOVER ARQUIVOS DE UMA PASTA PARA OUTRA
#====================================================================
def musculos(diretorio_origem,diretorio_final,dicionario_series):
    """
    essa função é responsável por mover os arquivos de uma área para a área destinada
    a função escaneia a pasta e se houver duplicados, ela cria outra pasta com o mesmo nome da série
    
    args:
        diretorio_origem (str): é o caminho absoluto do diretório onde estão os arquivos para serem movidos

        diretorio_final (str): é o caminho absoluto do diretório onde os arquivos serão movidos

        dicionario_series (dict): é um dicionário onde a chave é o nome da série e o valor é a lista contendo os nomes dos arquivos

    """
    
    # criandob a pasta especifica de cada serie
    for serie in dicionario_series.keys():
        caminho_novo = os.path.join(diretorio_final,serie)
        if not os.path.exists(caminho_novo):
            os.makedirs(caminho_novo)
        
        # pegando os arquivos da serie
        caminho_secundario = caminho_novo

        for arquivo in dicionario_series[serie]:
            
            #verificando duplicados
            while True:
                if arquivo in os.listdir(caminho_secundario):
                    caminho_secundario = os.path.join(caminho_secundario,serie)
                    if not os.path.exists(caminho_secundario):
                         os.makedirs(caminho_secundario)
                else:
                    # Junta o caminho da pasta origem com o nome do ficheiro para obter o caminho absoluto
                    caminho_origem_completo = os.path.join(diretorio_origem, arquivo)
                    shutil.move(caminho_origem_completo, caminho_secundario)
                    break
