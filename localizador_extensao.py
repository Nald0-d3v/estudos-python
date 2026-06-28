# Localizador de Arquivos por Extensão

# Imports

import os


# Entrada do usuário

pasta = input("Endereço: ")
arquivos = os.listdir(pasta)

extensao = input("Qual a extensão deseja procurar? ")
extensao_m = extensao.lower()

if not extensao_m.startswith("."):
    extensao_m = "." + extensao_m


# Localizar arquivos

total = 0

for arquivo in arquivos:

    caminho = os.path.join(pasta, arquivo)
    arquivo_m = arquivo.lower()

    if os.path.isdir(caminho):
        continue

    if arquivo_m.endswith(extensao_m):
        print("-", arquivo)
        total += 1


# Resultado

print("Total:", total)