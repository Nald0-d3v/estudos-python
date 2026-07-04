import requests

# Consulta de País

print("Digite apenas o nome do país em inglês.")

while True:

    # Entrada

    pais = input("Digite o país (ou 'sair'): ")

    # Sair

    if pais.lower() == "sair":
        print("Programa encerrado.")
        break

    # Validação

    if any(letra.isdigit() for letra in pais):
        print("O nome do país não pode conter números.")
        continue

    # Consulta da API

    url = "https://countries.dev/name/" + pais

    resposta = requests.get(url)

    # Verificar resposta

    if resposta.status_code != 200:
        print("País não encontrado.")
        continue

    # Dados

    dados = resposta.json()

    print("\nPaíses encontrados:")

    for indice, pais_item in enumerate(dados):
        print(f"{indice} - {pais_item['name']}")

    # Escolha do usuário

    try:
        escolha = int(input("Escolha o número do país: "))

        if escolha < 0 or escolha >= len(dados):
            print("Número inválido.")
            continue

    except ValueError:
        print("Digite apenas números.")
        continue

    pais_encontrado = dados[escolha]

    # Resultado

    print()

    print("Nome:", pais_encontrado["name"])

    if "capital" in pais_encontrado:
        print("Capital:", pais_encontrado["capital"])
    else:
        print("Capital: Não disponível")

    if "region" in pais_encontrado:
        print("Região:", pais_encontrado["region"])

    if "subregion" in pais_encontrado:
        print("Sub-Região:", pais_encontrado["subregion"])

    if "population" in pais_encontrado:
        print("População:", pais_encontrado["population"])

    if "languages" in pais_encontrado and len(pais_encontrado["languages"]) > 0:
        print("Idioma:", pais_encontrado["languages"][0]["name"])
    else:
        print("Idioma: Não disponível")

    if "currencies" in pais_encontrado and len(pais_encontrado["currencies"]) > 0:
        print("Moeda:", pais_encontrado["currencies"][0]["name"])
        print("Símbolo:", pais_encontrado["currencies"][0]["symbol"])
    else:
        print("Moeda: Não disponível")

    print()