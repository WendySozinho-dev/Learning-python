#permutacao
from itertools import permutations

# Lista de valores
valores = [1, 2, 3]

# Gerar todas as permutações
permutacoes = permutations(valores)

# Iterar sobre as permutações
for permutacao in permutacoes:
    # Iterar sobre cada valor na permutação (que é uma tupla)
    for valor in permutacao:
        print(valor, end=" ")  # Imprimir cada valor
    print()  # Nova linha para separar as permutações
    