from tools.Menu import menu
from tools.Get_input import get_input
from tools.Musculos import musculos
from tools.Visao import visao
from tools.Existencia import existe
from tools.Analisador import analisador
from tools.explorerNGC import explorerNGC
from tools.Json_io import json_read, json_write, json_scan
from tools.Radar import radar
from tools.Scanner import scanner
import json
import os
import re
import shutil
import textual




def write(txt):
    length = len(txt)
    for c in range(0,length):
        print('_',end = '')
    print(f"\n\033[33m{txt}\033[m")
    for c in range(0,length):
        print('#', end = '')
    print()



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
        write('varredura inicial realisada!')
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
comands = (
            'sair',
            'organizar os diretórios de séries',
            'habilitar organisação dos diretórios na inicialização',
            'que programa é esse?',
            'adicionar diretório de vasculha',
            'eliminar diretorio de vasculha',
            'desabilitar organisação dps diretórios na inicialização',
            'procurar um item em todo armazenamento interno'
          )
while True:
    menu(items = comands)
    user_input = get_input(message = 'digite o comando ', item_type = int)
    if existe(item = user_input, lista = comands):
        if user_input == 1:
            print("saindo")
            break

        elif user_input == 2:
            integrador()

        elif user_input == 3:
            ngc_init['varredura_automatica'] = True
            json_write(path = '', file = 'ngc_init.json', dictionary = ngc_init)
            print('opção varredura automática ativada em ngc_init.json')

        elif user_input == 4:
            print('esse é um programa que auxilia na organisação de arquivos\ninicialmente pensado para só mover séries de uma pasta específica para outra')
            print('agora, ele deve ser capaz de mover arquivos de múltiplas pastas\ndeve também ter a opção de pesquisa para rastrear arquivos do seu armazenamento interno\ne guardar na pasta selecionada')
            

        elif user_input == 5:
            input('selecione o diretório origem\n[enter para continuar]  ')
            initial_dir = explorerNGC().run()
            input('selecione o diretório onde irão esses arquivos\n[enter para continuar]  ')
            final_dir = explorerNGC().run()
            # agora, vamos gravar esses diretórios
            ngc_init['inicio'].append(initial_dir)
            ngc_init['fim'].append(final_dir)
            json_write(path = '',file = 'ngc_init.json', dictionary = ngc_init)
            print('escrita concluida')
        
        elif user_input == 6:
            write('eis os diretorios registrados')
            # imprimindo os diretórios
            counter = 0
            for c in ngc_init['inicio']:
                print(f"\033[31m{counter+1}\033[m de:")
                write(c)
                print(f"\033[31m{counter+1}\033[m para:")
                write(ngc_init['fim'][counter])
                counter += 1
            # pegando a escolha do usuario
            entrada = get_input(message = '\033[35mdigite o número do diretório\033[m', item_type = int)
            if existe(item = entrada, lista = ngc_init['inicio']):
                del ngc_init['inicio'][entrada-1]
                del ngc_init['fim'][entrada-1]
                json_write(file = 'ngc_init.json', path = '', dictionary = ngc_init)
                write('diretório removido no radar de vasculha com sucesso!')
            else:
                write('opção inválida')

        elif user_input == 7:
            ngc_init['varredura_automatica'] = False
            json_write(path='',file = 'ngc_init.json', dictionary = ngc_init)
            write('varredura automática desabilitada com sucesso')

        elif user_input == 8:
            # pegando a raiz
            android_root = '/storage/emulated/0'
            this_root = os.path.expanduser("~")
            main_root = ''
            
            if android_root != this_root:
                menu(items = (android_root,this_root), header = 'escolha uma dessas raíses')
                entrada = get_input(message = 'digite o numero da opção  ')
                while not existe(item = entrada, lista = (android_root,this_root)):
                    entrada = get_input(item_type = int, message = 'opção inválida, tente de novo  ')
                if entrada == 1:
                    main_root = android_root
                else:
                    main_root = this_root
                    
            else:
                main_root = this_root

            # agora, vamos varrer o armazenamento interno
            print('varrendo o armazenamento')
            internal_storage = radar(main_root)
            print('varredura concluida')
            # agora, vamos perguntar ao usuário se ele quer fazer uma busca aproximada ou busca literal
            scanner_options = ('procurar por aproximação','prcura literal')
            menu(items = scanner_options, header = 'método de busca')
            entrada = get_input(message = 'digite o número do comando  ',item_type = int)
            if existe(entrada,scanner_options):
                if entrada == 1:
                    entrada = ''
                    while entrada != '//':
                        entrada = input('\n\n\033[36mdigite o que procura digite // para parar\033[m  ')
                        found_items = scanner(standard_text = entrada, files = internal_storage)
                        print(f'\n\n{found_items}')
                else:
                    print('opção em construção (- -)')
            
        
    else:
        print('comando inexistente')







    
    