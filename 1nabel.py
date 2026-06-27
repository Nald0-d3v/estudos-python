import os
import shutil

pasta = input("Qual pasta deseja organizar? ")
arquivos = os.listdir(pasta)

pasta_textos = os.path.join(pasta, "Textos")
pasta_imagens = os.path.join(pasta, "Imagens")
pasta_pdfs = os.path.join(pasta, "Pdfs")

if not os.path.exists(pasta_textos):
    os.mkdir(pasta_textos)

if not os.path.exists(pasta_imagens):
    os.mkdir(pasta_imagens)

if not os.path.exists(pasta_pdfs):
    os.mkdir(pasta_pdfs)

moveu_arquivo = False

for arquivo in arquivos:
    caminho_arquivo = os.path.join(pasta, arquivo)

    if arquivo.lower().endswith(".txt"):
        shutil.move(caminho_arquivo, pasta_textos)
        print(arquivo, "movido para Textos")
        moveu_arquivo = True

    elif arquivo.lower().endswith(".png") or arquivo.lower().endswith(".jpg"):
        shutil.move(caminho_arquivo, pasta_imagens)
        print(arquivo, "movido para Imagens")
        moveu_arquivo = True

    elif arquivo.lower().endswith(".pdf"):
        shutil.move(caminho_arquivo, pasta_pdfs)
        print(arquivo, "movido para Pdfs")
        moveu_arquivo = True

if not moveu_arquivo:
    print("Nenhum arquivo encontrado para organizar.")
else:
    print("Arquivos organizados!")

    #Oi hoje quero dar uma revisada nesse codigo, pode me explicar novamente as funções?