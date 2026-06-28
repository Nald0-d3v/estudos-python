# Contador de PDFs

# Imports

import os


# Entrada do usuário

pasta = input("Endereço: ")
arquivos = os.listdir(pasta)


# Contador

numero = 0


# Contagem dos PDFs

for arquivo in arquivos:

    arquivo_m = arquivo.lower()
    caminho = os.path.join(pasta, arquivo)

    if os.path.isdir(caminho):
        continue

    if arquivo_m.endswith(".pdf"):
        numero += 1


# Resultado

print(numero, "arquivo(s) PDF encontrado(s)")