import random

# Gerar um número inteiro aleatório entre 1 e 10
numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)
print("escolheum numero aleatorio de 1 a 10")

# Selecionar um elemento aleatório de uma lista
lista = [1, 2, 3, 4, 5]
elemento_aleatorio = random.choice(lista)
print(elemento_aleatorio)
print("escolhe um elemento aleatorio da lista")

# Embaralhar uma lista
lista = [1, 2, 3, 4, 5]
random.shuffle(lista)
print(lista)
print("lista embaralhada")

# Gerar uma amostra aleatória de 3 elementos de uma lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
amostra = random.sample(lista, 3)
print(amostra)
print("vai pegar 3 amostras aleatorias na lista")

