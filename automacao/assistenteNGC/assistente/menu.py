# aqui vou criar o menu

def menu(items = ["none","none"],header = "assistenteNGC", int_counter = True, str_counter = ["->","=>"] ):
    items_number = len(items)
    
    # criando o cabecalho
    header_line = len(header)+2
    line(limit = header_line)
    print(f"|\033[34m{header}\033[m|")
    line(limit = header_line, line = "^")

    
    # caso o precise deixar os items numerados
    if int_counter:
        counter = 1
        for i in items:
            print(f"{counter}: \033[33m{i}\033[m")
            counter +=1

# uma funcao para desenhar uma linha
def line(limit = 30, line = "_"):
    for c in range(0,limit):
        print(line, end = "")
    print()







line()

menu()
