# import os
# import shutil





# pasta = input("Digite: ")

# arquivos = os.listdir(pasta)
# pasta_imagens = os.path.join(pasta, "imagens")

# #funções


# #criar pasta:
# def criar_pasta(caminho):
#     if not os.path.exists(caminho):
#         os.mkdir(caminho)


# #mover arquivo:
# def mover_arquivo(origem, destino):
#     shutil.move(origem, destino)
#     print("arquivo", arquivo, "movido")

# #criar pastas
# criar_pasta(pasta_imagens)



# for arquivo in arquivos:
#     caminho = os.path.join(pasta, arquivo)
#     arquivo_minusculo = arquivo.lower()

#     if arquivo_minusculo.endswith((".png", ".jpg")):

#         mover_arquivo(caminho, pasta_imagens)


# print("processo encerrado.")








# import os


# pasta = input("digite o endereço: ")

# arquivos = os.listdir(pasta)


# numero = 1

# for arquivo in arquivos:

#     caminho = os.path.join(pasta, arquivo)
#     arquivo_minusculo = arquivo.lower()

#     novo_nome = "figura_" + str(numero) + ".png"

#     if arquivo_minusculo.endswith(".png"):

#         arquivo_novo = os.path.join(pasta, novo_nome)

#         os.rename(caminho, arquivo_novo)

#         numero +=1

#         print(arquivo, "renomeado para", novo_nome)









import os

pasta = input("Endereço: ")
arquivos = os.listdir(pasta)


numero = 1

for arquivo in arquivos:

    arquivo_minusculo = arquivo.lower()
    caminho = os.path.join(pasta, arquivo)

    nome, extensao = os.path.splitext(arquivo)

    novo_nome = "Imagem_" + str(numero) + extensao

    arquivo_novo = os.path.join(pasta, novo_nome)

    os.rename(caminho, arquivo_novo)
    print(arquivo, "renomeado para", novo_nome)

    numero += 1


#o que eu sinto agora é que eu so copiei o que vc me mandou, nao sei ao certo se to tendo real progresso