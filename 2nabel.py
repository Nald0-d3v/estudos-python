import os
import shutil



pasta = input("Digite o endereço: ")
arquivos = os.listdir(pasta)

#caminhos

pasta_textos = os.path.join(pasta, "Textos")
pasta_imagens = os.path.join(pasta, "Imagens")
pasta_videos = os.path.join(pasta, "Videos")
pasta_outros = os.path.join(pasta, "Outros")

#veficação e criação de pastas

if not os.path.exists(pasta_textos):
    os.mkdir(pasta_textos)

if not os.path.exists(pasta_imagens):
    os.mkdir(pasta_imagens)

if not os.path.exists(pasta_videos):
    os.mkdir(pasta_videos)

if not os.path.exists(pasta_outros):
    os.mkdir(pasta_outros)

#mover arquivos

moveu_arquivo = False

for arquivo in arquivos:
    arquivo_minusculo = arquivo.lower()

    caminho_arquivo = os.path.join (pasta, arquivo)

    if os.path.isdir(caminho_arquivo):
        continue

    if arquivo_minusculo.endswith(".txt"):
        shutil.move(caminho_arquivo, pasta_textos)
        moveu_arquivo = True

    elif arquivo_minusculo.endswith(".png"):
        shutil.move(caminho_arquivo, pasta_imagens)
        moveu_arquivo = True

    elif arquivo_minusculo.endswith((".mp4", ".mov")):
        shutil.move(caminho_arquivo, pasta_videos)
        moveu_arquivo = True
    
    else:
        shutil.move(caminho_arquivo, pasta_outros)
        moveu_arquivo = True



if not moveu_arquivo:
    print("nenhum arquivo encontrado.")

else:
    print("arquivos movidos.")













# import os
# import shutil


# pasta = input("endereço: ")

# arquivos = os.listdir(pasta)

# pasta_texto = os.path.join(pasta, "Texto")

# if not os.path.exists(pasta_texto):
#     os.mkdir(pasta_texto)

# moveu = False

# for arquivo in arquivos:
#     arquivo_minusculo = arquivo.lower()


#     caminho_arquivo = os.path.join(pasta, arquivo)

#     if arquivo_minusculo.endswith(".txt"):
#         shutil.move(caminho_arquivo, pasta_texto)
#         moveu = True


# if not moveu:
#     print("sem arquivos")


# else:
#     print("Concluido")

# #fiz eu mini mas parece que nao ta funcionando