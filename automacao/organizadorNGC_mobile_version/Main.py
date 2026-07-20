from tools.Menu import menu
from tools.Get_input import get_input
from tools.Musculos import musculos
from tools.Visao import visao
from tools.Existencia import existe
from tools.explorerNGC import explorerNGC
from tools.Json_io import json_read, json_write, json_scan
import json
import os

# primeiro, detectar se existe o arquivo de inicialização
ngc_init = {}
try:
    with open("ngc_init.json","r") as file:
        ngc_init = json.load(file)
except FileNotFoundError:
    input("não existe um arquivo de inicialização\npressione [enter] para abrir o explorador  ")
    initial_dir = explorerNGC().run()
    input("agora o diretorio final\n[enter para continuar]   ")
    final_dir = explorerNGC().run()

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

    
    