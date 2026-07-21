# função para escrever e ler um json no armazenamento interno
import json
import os
# função que escaneia um arquivo json
def json_scan(path,file):
    #verificando se a a pasta existe
    if not os.path.exists(os.path.join(path, file)):
        print(f"{os.path.join(path, file)} não é um diretório")
        return False
    
    # verificando a terminacao
    if file[-5::] != ".json":
        print(f"{file} não é um json!")
        return False
    else:
        return file

# função de leitura
def json_read(path,file):
    file_content = {}
    diretory = os.path.join(path,file)
    try:
        with open(diretory, "r") as f:
            file_content = json.load(f)

    except Exception as e:
        print(e)
    else:
        return file_content


# função de escrita
def json_write(path,file,dictionary):
    diretory = os.path.join(path,file)
    with open(diretory,'w', encoding = 'utf-8') as f:
        json.dump(dictionary, f, indent = 4, ensure_ascii = False)
            



