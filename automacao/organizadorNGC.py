import re
import os
import json
import shutil

def analizador(teste):
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
    padrao3 = re.compile(r"(.+)[sS](\d+)[eE](\d+)(\.\w)")

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


def existe(item, lista):  
    """ 
    confirma se o item, que é um numero inteiro, está entre len(lista)
    
    args:
        item (int):  o item que queremos verificar a existência na lista

        lista (list): a lista onde queremos verificar o item

    returns:
        bool: retorna True se o item estiver entre len(lista) e False se for o contrário
    """
    valor = leiaint(item)
    caixa = len(lista)
    if valor > 0 and valor <= caixa:
        return True
    else:
        return False

def escreva(txt):  
    """
    responsavel por imprimir algo na tela de forma mais estilosa
    
    args:
        txt: o texto a ser escrito na tela

    returns:
        None: nada é retornado
    """
    cont = 0
    for c in txt:
        cont += 1
    linha(cont, "-")
    print(f"\033[33m{txt}\033[m")
    linha(cont)

def linha(param=30, linha="_"):  
    """
    responsavel por imprimir uma linha simples

    args:
        param (int): o número máximo, até onde a linha vai
        
        linha (str): o que constitui a linha
    """
    for c in range(0, param):
        print(linha, end="")
    print()

def menu(lista, cabecalho="menu", contador=(1), espaco=""):
    """
    responsavel por criar um simples menu

    args:
        lista (list,tuple): a lista de itens que que o menu exibirá

        cabecalho (str): o cabeçalho do menu, o que será exibido no topo

        contador (int,str,list): o valor que aparecerá na esquerda de cada item
        
        espaco (str): o espaço entre o contador e o item

    """
    cont = 0
    escreva(cabecalho)
    try:
        cont = int(contador)
        linha()
        for c in lista:
            print(f"{cont}:\033[36m{c}\033[m")
            cont += 1
        linha()
    except:
        linha()
        cont = 0
        limite = len(contador)
        for c in lista:
            if cont > limite - 1:
                cont = 0
            print(f"{contador[cont]}:{espaco}\033[36m{c}\033[m")
            cont += 1
        linha()

def leiaint(valor):
    """
    responsavel por ler um numero inteiro e retorna esse valor

    args:
        valor (str): o caractere que será convertido em um valor inteiro

    returns:
            int: o valor garantido que é um inteiro
    """
    num = 0
    while True:
        try:
            num = int(valor)
        except:
            print(f"{valor} nao e um numero inteiro")
            valor = str(input("tente novamente\n"))
        else:
            return num

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


#==========================================================
# O CÉREBRO: PROCESSA, QUESTIONA E GERENCIA
# ==========================================================

# para armazenamento dos dados, ao invez de usar um txt, usarei um JSON
configuracao = {}
try:
    with open("ngc_init.json","r",encoding = 'utf-8') as arquivo:
        configuracao = json.load(arquivo)
except FileNotFoundError:

    raiz_principal = os.path.expanduser("~")
    
    sistemas = ("android","windous","linux")
    menu(cabecalho = "sistemas",lista = sistemas)
    while True:
        entrada = str(input("digite o numero da opcao do seu sistema operacional    "))
        entrada = leiaint(entrada)
        if existe(entrada,sistemas):
            break

    if entrada == 1:
        raiz_android = "/storage/emulated/0"
        if raiz_android != raiz_principal:
            print("detectei que estas a usar algum aplicativo como termux!")
            menu(cabecalho = "pretende usar", lista=(raiz_principal, raiz_android))
            entrada_menu = leiaint(input())

            # verificando a raiz selecionada
            if entrada_menu == 1:
                raiz = raiz_principal
            else:
                raiz = raiz_android
        
        # validando o caminho digitado pelo usuario no Android
        while True:
            entrada_inicial_pasta = str(input("digite o caminho dos arquivos (ex: download/animes):\n"))
            entrada_inicial_usuario = os.path.join(raiz, entrada_inicial_pasta.replace("\\", "/").lstrip("/"))

            lista_caotica = visao(entrada_inicial_usuario)

            if lista_caotica is not False:  # A visão retornou dados!
                break
            else:
                escreva("erro, diretorio inexistente no android")
        
        while True:
            entrada_final_pasta = str(input("digite o caminho final dos arquivos\n(\033[33mpara onde os arquivos irao\033[m)\n"))
            entrada_final_usuario = os.path.join(raiz, entrada_final_pasta.replace("\\","/").lstrip("/"))
            
            lista_caotica = visao(entrada_final_usuario)

            if lista_caotica is not False:
                break
            else:
                escreva("erro, diretorio i.existente no android")
                

    else:
        # Se for PC, usamos a home expansível
        raiz = raiz_principal

        # validando o caminho digitado pelo usuario no PC
        while True:
            entrada_pasta = str(input("digite o diretorio use [\\ ou /] como separador ex: downloads/series:\n"))
            # validando o caminho para windous
            if entrada == 2:
                entrada_limpa = entrada_pasta.replace("/", "\\").lstrip("\\")
            # validando o caminho para linux
            else:
                entrada_limpa = entrada_pasta.replace("\\", "/").lstrip("/")
            # Junta a raiz Home do PC com a pasta limpa
            entrada_inicial_usuario = os.path.join(raiz, entrada_limpa)

            lista_caotica = visao(entrada_inicial_usuario)

            if lista_caotica is not False:  # A visão retornou dados!
                break
            else:
                escreva("erro diretorio invalido tente novamente")

        del lista_caotica
        while True:
            entrada_pasta = str(input("digite o diretorio para onde vao os arquivos\n"))
            if entrada == 2:
                entrada_limpa = entrada_pasta.replace("/","\\").lstrip("\\")
            else:
                entrada_limpa = entrada_pasta.replace("\\","/").lstrip("/")
            entrada_final_usuario = os.path.join(raiz,entrada_limpa)

            lista_caotica = visao(entrada_final_usuario)

            if lista_caotica is not False:
                break
            else:
                escreva("diretorio invalido tente novamente")
            del lista_caotica
            
    configuracao["origem"] = entrada_inicial_usuario
    configuracao["fim"] = entrada_final_usuario
    #escrevendo tudo no ngc_init.json
    with open("ngc_init.json","w",encoding = 'utf-8') as arquivo:
        json.dump(configuracao,arquivo,indent = 4, ensure_ascii = False)
            

except:
    escreva("ocoreu um erro  isso nao e o seu problema, mas sim do programador!")

else:
    # listando todos os arquivos do diretorio inicial
    extensoes = (".mp4",".mkv",".avi",".webm")
    arquivos_brutos = visao(configuracao["origem"])

    escreva("eis os arquivos brutos")
    print(arquivos_brutos)
    videos = list()

    for arquivo in arquivos_brutos:
        nome,extensao = os.path.splitext(arquivo)
        if extensao in extensoes:
            videos.append(arquivo)
    

    del arquivos_brutos

    escreva("eis os videos")
    print(videos)


    lista_de_videos = analizador(videos)
    del videos

    # movendo os arquivos para o diretorio exato
    musculos(configuracao["origem"],configuracao["fim"],lista_de_videos)
