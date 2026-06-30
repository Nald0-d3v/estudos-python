import requests

# Consulta de usuário do GitHub

while True:

    # Entrada

    usuario = input("Digite o usuário do GitHub (ou 'sair'): ")
    usuario_m = usuario.lower()

    # Sair

    if usuario_m == "sair":
        print("Programa encerrado.")
        break

    # Consulta da API

    url = "https://api.github.com/users/" + usuario

    resposta = requests.get(url)
    dados = resposta.json()

    # Verificar usuário

    if "message" in dados:
        print("Usuário não encontrado.")
        continue

    # Resultado

    print()
    print("Usuário:", dados["login"])
    print("Seguidores:", dados["followers"])
    print("Seguindo:", dados["following"])
    print("Repositórios públicos:", dados["public_repos"])
    print("Conta criada em:", dados["created_at"])
    print()