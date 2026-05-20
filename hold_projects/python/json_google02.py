import json

with open('nome_do_arquivo.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

# Agora você pode acessar os dados
# Exemplo:
# print(dados['chave'])