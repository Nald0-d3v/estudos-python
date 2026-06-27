# Organizador v1

import os
import shutil


# funções


def criar_pasta(caminho):
    if not os.path.exists(caminho):
        os.mkdir(caminho)


def mover_arquivo(origem, destino):
    shutil.move(origem, destino)


def contar_arquivos(arquivos, pasta):

    imagem = 0
    texto = 0
    outros = 0

    for arquivo in arquivos:

        caminho = os.path.join(pasta, arquivo)

        if os.path.isdir(caminho):
            continue

        arquivo_minusculo = arquivo.lower()

        if arquivo_minusculo.endswith((".png", ".jpg")):
            imagem += 1

        elif arquivo_minusculo.endswith(".txt"):
            texto += 1

        else:
            outros += 1

    return imagem, texto, outros


# pegar endereço

while True:

    pasta = input("Endereço: ")

    if os.path.isdir(pasta):
        break

    else:
        print("Digite um endereço válido.")


arquivos = os.listdir(pasta)


# contar arquivos

imagem, texto, outros = contar_arquivos(arquivos, pasta)

total = imagem + texto + outros


print("Imagens:", imagem)
print("Textos:", texto)
print("Outros:", outros)
print("Total:", total)


# perguntar

while True:

    resposta = input("Deseja organizar os arquivos? (s/n): ")

    if resposta.lower() in ("s", "n"):
        break

    else:
        print("Resposta inválida.")


# organizar

if resposta.lower() == "s":

    print("Organizando...")


    pasta_imagens = os.path.join(pasta, "imagens")
    pasta_textos = os.path.join(pasta, "textos")
    pasta_outros = os.path.join(pasta, "outros")


    criar_pasta(pasta_imagens)
    criar_pasta(pasta_textos)
    criar_pasta(pasta_outros)


    for arquivo in arquivos:

        caminho = os.path.join(pasta, arquivo)

        if os.path.isdir(caminho):
            continue


        arquivo_minusculo = arquivo.lower()


        if arquivo_minusculo.endswith((".png", ".jpg")):
            mover_arquivo(caminho, pasta_imagens)


        elif arquivo_minusculo.endswith(".txt"):
            mover_arquivo(caminho, pasta_textos)


        else:
            mover_arquivo(caminho, pasta_outros)


    print(total, "arquivo(s) movido(s)")


elif resposta.lower() == "n":

    print("Programa encerrado.")