#contador de PDFs

# import os
# import shutil


# pasta = input("Endereço: ")

# arquivos = os.listdir(pasta)


# numero = 0

# for arquivo in arquivos:
#     arquivo_m = arquivo.lower()

#     caminho = os.path.join(pasta, arquivo)

#     if os.path.isdir(caminho):
#         continue

#     if arquivo_m.endswith(".pdf"):
#         numero +=1


# print(numero, "arquivos PDF(s)")





# Listar Arquivos


import os


pasta = input("Endereço: ")

arquivos = os.listdir(pasta)


texto = 0
pdf = 0
imagem = 0
outro = 0


print("PDFs encontrados: ")

for arquivo in arquivos:
    
    arquivo_m = arquivo.lower()

    caminho = os.path.join(pasta, arquivo)

    if os.path.isdir(caminho):
        continue


    if arquivo_m.endswith(".txt"):
        texto +=1


    elif arquivo_m.endswith(".pdf"):
        pdf +=1
        print("-", arquivo)


    elif arquivo_m.endswith((".png", ".jpg")):
        imagem +=1


    else:
        outro +=1    

total = texto + pdf + imagem + outro

print("Textos:", texto)
print("PDFs:", pdf)
print("Imagens:", imagem)
print("Outros", outro)
print("Total:", total)

#entao é isso? qual o proximo passo?