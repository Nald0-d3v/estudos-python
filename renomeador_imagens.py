# Renomeador de Imagens

# Imports

import os


# Entrada do usuário

pasta = input("Endereço: ")
arquivos = os.listdir(pasta)


# Renomear imagens

numero = 0

for arquivo in arquivos:

    arquivo_minusculo = arquivo.lower()
    caminho = os.path.join(pasta, arquivo)

    nome, extensao = os.path.splitext(arquivo)
    novo_nome = "Imagem_" + str(numero) + extensao

    arquivo_novo = os.path.join(pasta, novo_nome)


    if arquivo_minusculo.endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp")):

        os.rename(caminho, arquivo_novo)
        print(arquivo, "renomeado para", novo_nome)
        numero += 1

print("Total de imagens renomeadas:", numero)