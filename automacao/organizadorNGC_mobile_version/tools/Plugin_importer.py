# funcao responsavel por importar modulos do pluguin dinamicamente
import importlib
import os

def importer(path):

    brute_content = os.listdir(path)
    python_modules = list()
    temp_list = list()

    for c in brute_content:
        if ".py" in c[-3::]:
            temp_list.append(c[-4::-1])

    print(temp_list)
    
    for c in temp_list:
        python_modules.append(c[::-1])
    print(python_modules)



importer(path="testes/")
        

