# Contador de Arquivos

# Imports

import os


# Entrada do usuário

pasta = input("Endereço: ")
arquivos = os.listdir(pasta)


# Contadores

texto = 0
pdf = 0
imagem = 0
outro = 0


# Listar PDFs

print("PDFs encontrados:")


# Contagem

for arquivo in arquivos:

    arquivo_m = arquivo.lower()
    caminho = os.path.join(pasta, arquivo)

    if os.path.isdir(caminho):
        continue

    if arquivo_m.endswith(".txt"):
        texto += 1

    elif arquivo_m.endswith(".pdf"):
        pdf += 1
        print("-", arquivo)

    elif arquivo_m.endswith((".png", ".jpg")):
        imagem += 1

    else:
        outro += 1


# Resultado

total = texto + pdf + imagem + outro

print("Textos:", texto)
print("PDFs:", pdf)
print("Imagens:", imagem)
print("Outros:", outro)
print("Total:", total)