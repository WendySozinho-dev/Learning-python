import json

# Dados a serem escritos
dados = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

# Nome do arquivo
nome_arquivo = "dados.json"

# Abre o arquivo em modo de escrita
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    # Escreve os dados no arquivo JSON
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)

print(f"Dados salvos em {nome_arquivo}")
#modo de leitura
with open(nome_arquivo,"r",encoding="utf-8") as f:
    java=json.loads(f.read())
    for k in java.keys():
        print(k)