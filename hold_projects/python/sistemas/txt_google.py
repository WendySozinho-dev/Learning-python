def remover_item_de_txt(nome_arquivo, item_a_remover):
    """
    Remove uma linha específica de um arquivo TXT.

    Args:
        nome_arquivo: O caminho para o arquivo TXT.
        item_a_remover: A string exata a ser removida do arquivo.
    """
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()

        with open(nome_arquivo, 'w') as arquivo:
            for linha in linhas:
                if item_a_remover not in linha:
                    arquivo.write(linha)
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


# Exemplo de uso:
nome_do_arquivo = "meu_arquivo.txt"
item_para_remover = "item_a_remover"

# Cria um arquivo de exemplo se ele não existir
import os
if not os.path.exists(nome_do_arquivo):
    with open(nome_do_arquivo, 'w') as f:
        f.write("linha 1\n")
        f.write("item_a_remover\n")
        f.write("linha 2\n")
        f.write("outra_linha\n")

remover_item_de_txt(nome_do_arquivo, item_para_remover)