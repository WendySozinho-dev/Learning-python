# funcao que vai pegar e tratar o input do usuario

def get_input(item_type = int, message = "digite algo"):   
    

    """ funcao responsavel por tratar a entrada
    e garantir que o usuario digitou o tipo de dado certo

        item_type:
            o tipo de dado que queremos verificar
            
            args:
                int:
                   tipo inteiro
                float:
                    tipo flutuante
                str:
                    cadeia de caracteres
        message:
            a primeira mensagem que aparecera para o usuario

            args:
                str:
                    um texto comun
    """

    
    if item_type == int : 
        number = get_int(input(f"{message}  "))
        return number
    elif item_type == float:
        number = get_float(input(f"{message}  "))
        return number
    elif item_type == bool:
        number = get_bool(input(f"{message}  "))
        return number



def get_float(char):
    number = ""
    while True:
        try:
            number = float(char)
        except ValueError:
            char = input("tente novamente   ")
        else:
            break
    return number


def get_int(char):  
    number = ""
    while True:
        try:
            number = int(char)
        except ValueError:      
            char = input("tente novamente   ")
        else:
            break
    return number


def get_bool(char):
    while True:
        if char not in ("True","False","0","1"):
            char = input("tente novamente   ")
        else:
            char = bool(char)
            break
    return char           

