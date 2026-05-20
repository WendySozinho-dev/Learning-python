# Criar um novo arquivo ou sobrescrever um existente
with open("meu_arquivo.txt", "w") as arquivo:
    arquivo.write("Este é o meu primeiro arquivo de texto.\n")
    arquivo.write("Adicionando mais uma linha.\n")

# Adicionar conteúdo a um arquivo existente
with open("meu_arquivo.txt", "a") as arquivo:
    arquivo.write("Adicionando mais uma linha ao final.\n")
