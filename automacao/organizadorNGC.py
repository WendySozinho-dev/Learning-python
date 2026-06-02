import re
import os
import json
import shutil

def analizador(teste):

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


def existe(item, lista):  # confirma se o item, que e um numero inteiro, se esta entre len(lista)
    valor = leiaint(item)
    caixa = len(lista)
    if valor > 0 and valor <= caixa:
        return True
    else:
        return False

def escreva(txt):  # responsavel por imprimir algo na tela de forma mais estilosa
    cont = 0
    for c in txt:
        cont += 1
    linha(cont, "-")
    print(f"\033[33m{txt}\033[m")
    linha(cont)

def linha(param=30, linha="_"):  # responsavel por imprimir uma linha simples
    for c in range(0, param):
        print(linha, end="")
    print()

def menu(lista, cabecalho="menu", contador=(1), espaco=""):  # responsavel por criar um simples menu
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

def leiaint(valor):  # responsavel por ler um numero inteiro e retorna esse valor
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
    if os.path.exists(caminho) and os.path.isdir(caminho):
        conteudo_bruto = os.listdir(caminho)
        return conteudo_bruto
    else:
        return False

#====================================================================
# OS MUSCULOS: ENCARREGADOS DE MOVER ARQUIVOS DE UMA PASTA PARA OUTRA
#====================================================================
def musculos(diretorio_origem,diretorio_final,dicionario_series):
    
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
try:
    with open("ngc_init.json","r"):
        pass
except FileNotFoundError:

    while True:
        sistemas = ("android","windous","linux")
        menu(cabecalho = "sistemas",lista = sistemas)
        entrada = str(input("digite o numero da opcao do seu sistema operacional    "))
        entrada = leiaint(entrada)

        if existe(entrada,sistemas):
            break

    if entrada == 1:
        raiz_android = "/storage/emulated/0"
        if raiz_android != raiz_principal:
            print("detectei que estas a usar algum aplicativo como termux!")
            menu(cabecalho="pretende usar", lista=(raiz_principal, raiz_android))
            entrada_menu = leiaint(input())

            # verificando a raiz selecionada
            if entrada_menu == 1:
                raiz = raiz_principal
            else:
                raiz = raiz_android
        
        # validando o caminho digitado pelo usuario no Android
        while True:
            entrada_pasta = str(input("digite o caminho dos arquivos (ex: download/animes):\n"))
            entrada_usuario = os.path.join(raiz, entrada_pasta.replace("\\", "/").lstrip("/"))

            lista_caotica = visao(entrada_usuario)

            if lista_caotica is not False:  # A visão retornou dados!
                break
            else:
                escreva("erro, diretorio inexistente no android")

    else:
        # Se for PC, usamos a home expansível
        raiz = raiz_principal

        # validando o caminho digitado pelo usuario no PC
        while True:
            entrada_pasta = str(input("digite o diretorio use [\\ ou /] como separador ex: downloads/series:\n"))
            if entrada == 2:
                entrada_limpa = entrada_pasta.replace("/", "\\").lstrip("\\")
            else:
                entrada_limpa = entrada_pasta.replace("\\", "/").lstrip("/")
            # Junta a raiz Home do PC com a pasta limpa
            entrada_usuario = os.path.join(raiz, entrada_limpa)

            lista_caotica = visao(entrada_usuario)

            if lista_caotica is not False:  # A visão retornou dados!
                break
            else:
                escreva("erro diretorio invalido tente novamente")

    # Exibe o troféu final capturado pela visão
    print("\n\033[32m[Conteúdo Bruto Capturado pela Visão]:\033[m")
    print(lista_caotica)




