# aqui vou criar o menu
def menu(items = ["none","none"],header = "assistenteNGC", int_counter = True, str_counter = ["->","=>"] ):    
    # procurando o item mais longo da lista
    big_item = big_string(items)
        
    # criando o cabecalho
    header_line = len(header)+2
    line(limit = header_line)
    print(f"|\033[34m{header}\033[m|")
    line(limit = header_line, line = "^")

    counter_number = len(items)
    
    # caso o precise deixar os items numerados
    if int_counter:
        counter_number = len(items)
        line_width = len(big_item) + 4 + len(str(counter_number))
        line(limit = line_width)
        counter = 1
        for i in items:
            print(f"|{counter}: \033[33m{i}\033[m", end = "")
            # incrementando espacos para embelesar a caixa
            space_increased = len(big_item) - len(i) 
            
            print(" "*space_increased,end = "")
            print("|")
            counter +=1
        line(limit = line_width, line = "^")

    else:
        # caso o indicador de items seja personalizado
        counter_number = len(big_string(str_counter))
        line_width = len(big_item) + len(big_string(str_counter)) + len(str(counter_number)) +2
        point_objects = len(str_counter)
        line(limit = line_width)
        counter = 0
        # criando a caixa e depositando os itens
        for i in items:
            print(f"|{str_counter[counter]} \033[33m{i}\033[m", end = "")
            
            space_increased = len(big_item) - len(i) + (counter_number - len(str_counter[counter]))
           
            print(" "*space_increased,end = "")
            print("|")

            counter +=1
            if counter >= point_objects:
                counter = 0
        line(limit = line_width, line = "^")
                        

def big_string(items):
    # procurando o item mais longo da lista
    big_item = ""
    new_item = ""
    for item in items:
        new_item = item
        if len(new_item) > len(big_item):
            big_item = new_item


    return big_item

# uma funcao para desenhar uma linha
def line(limit = 30, line = "_"):
    for c in range(0,limit):
        print(line, end = "")
    print()

