from tools.Menu import menu
from tools.Get_input import get_input
from tools.Musculos import musculos
from tools.Visao import visao
from tools.Existencia import existe
from tools.Analisador import analisador
from tools.explorerNGC import explorerNGC
from tools.Json_io import json_read, json_write, json_scan
import json
import os
import re


def integrador():
       # varrendo as pastas iniciais
        clean_list = list()
        files = list()
        for diretory in ngc_init['inicio']:
            files.append(visao(diretory))
            # teremos listas dentro de lista
        
        # agora, vamos passar o pente fino nos arquivos
        for package in files:
            # agora, temos uma lista com dicionarios
            clean_list.append(analisador(package))        
        
        counter = 0 
        for diretory in ngc_init['fim']:
            # aqui vamos jogar os arquivos em seus respectivos diretorios
            musculos(diretorio_origem = ngc_init['inicio'][counter], diretorio_final = diretory, dicionario_series = clean_list[counter])
            counter += 1



# primeiro, detectar se existe o arquivo de inicialização
ngc_init = {}
initial_dir = ''
final_dir = ''
try:
    with open("ngc_init.json","r") as file:
        ngc_init = json.load(file)
except FileNotFoundError:
    input("não existe um arquivo de inicialização\npressione [enter] para abrir o explorador  ")
    initial_dir = explorerNGC().run()
    input("agora o diretorio final\n[enter para continuar]   ")
    final_dir = explorerNGC().run()
    # salvando os dados
    ngc_init['inicio'] = list()
    ngc_init['fim'] = list()
    ngc_init['varredura_automatica'] = False
    ngc_init['inicio'].append(initial_dir)
    ngc_init['fim'].append(final_dir)
    json_write(path = '',file = 'ngc_init.json', dictionary = ngc_init)

else:
    if ngc_init['varredura_automatica'] == True:
        # iniciando a varredura automática nos diretórios
        integrador()
"""
agora, no salvamento dos diretórios, não basta só dizer:
{
'inicio':'diretótio_inicial',
'fim':'diretório_final'
}
deve ter uma lista inicio e outra lista fim:
{
'inicio':['primeiro','segundo'],
'fim':['primeiro','segundo']
}
nota: o indice 1 do inicio tem como fim o indice 1 do fim 
assim podemos ter vários diretórios para vasculhar arquivos
"""

    



# aqui vamos criar um a inteface do sistema
comands = ('sair',
            'organizar o diretório',
            'organizar os diretórios na inicialização',
            'adicionar diretório de vasculha',
           'eliminar diretorio de vasculha')
while True:
    menu(items = comands)
    user_input = get_input(message = 'digite o comando ', item_type = int)
    if existe(item = user_input, lista = comands):
        if user_input == 1:
            print("saindo")
            break

        elif user_input == 2:
            pass

        elif user_input == 3:
            pass

        elif user_input == 4:
            pass

        elif user_input == 5:
            pass

        
    else:
        print('comando inexistente')







    
    