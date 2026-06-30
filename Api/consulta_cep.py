import requests

# Consulta de CEP - ViaCEP

while True:

    # Entrada

    cep = input("Digite o CEP (ou 'sair'): ")
    cep_m = cep.lower()

    # Sair

    if cep_m == "sair":
        print("Programa encerrado.")
        break

    # Validações

    if not cep.isdigit():
        print("CEP inválido. Digite apenas números.")
        continue

    if len(cep) != 8:
        print("O CEP deve conter exatamente 8 dígitos.")
        continue

    # Consulta da API

    url = "https://viacep.com.br/ws/" + cep + "/json/"

    resposta = requests.get(url)
    dados = resposta.json()

    # Verificar CEP

    if "erro" in dados:
        print("CEP não encontrado.")
        continue

    # Resultado

    print()
    print("CEP:", dados["cep"])
    print("Rua:", dados["logradouro"])
    print("Bairro:", dados["bairro"])
    print("Cidade:", dados["localidade"])
    print("Estado:", dados["uf"])
    print("DDD:", dados["ddd"])
    print()