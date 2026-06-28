# Organizador de Imagens

# Imports

import os
import shutil


# Funções

def criar_pasta(caminho):
    if not os.path.exists(caminho):
        os.mkdir(caminho)


def mover_arquivo(origem, destino):
    shutil.move(origem, destino)
    print("Arquivo", arquivo, "movido")


# Entrada do usuário

pasta = input("Digite o endereço: ")
arquivos = os.listdir(pasta)

pasta_imagens = os.path.join(pasta, "Imagens")


# Criar pasta

criar_pasta(pasta_imagens)


# Organizar imagens

for arquivo in arquivos:

    caminho = os.path.join(pasta, arquivo)
    arquivo_minusculo = arquivo.lower()

    if arquivo_minusculo.endswith((".png", ".jpg")):
        mover_arquivo(caminho, pasta_imagens)


# Resultado

print("Processo encerrado.")