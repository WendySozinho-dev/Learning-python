meu_dicionario = {"frutas": ["maçã", "banana"], "numeros": [10, 20]}

# Adicionando uma fruta
meu_dicionario["frutas"].append("laranja")
print(meu_dicionario["frutas"])  # Saída: ['maçã', 'banana', 'laranja']

# Removendo um número
meu_dicionario["numeros"].remove(10)
print(meu_dicionario["numeros"])  # Saída: [20]

# Inserindo um número
meu_dicionario["numeros"].insert(0, 5)
print(meu_dicionario["numeros"])  # Saída: [5, 20]

# Percorrendo as frutas
for fruta in meu_dicionario["frutas"]:
    print(fruta)

# Percorrendo os números
for numero in meu_dicalist["numeros"]:
    print(numero)