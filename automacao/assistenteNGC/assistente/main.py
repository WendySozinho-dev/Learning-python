from tools.Menu import  menu
from tools.Get_input import get_input



# espaco reservado para variaveis
comands = ("escutar comando","sair","repetir a fala")
entrada = ""

# iniciando o loop principal do assistente
while True:
    menu(comands)
    entrada = get_input(item_type = int)













