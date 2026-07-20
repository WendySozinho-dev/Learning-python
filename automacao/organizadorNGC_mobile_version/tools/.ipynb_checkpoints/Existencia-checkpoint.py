# função que verifica a existencia

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
