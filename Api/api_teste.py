import requests

url = "https://jsonplaceholder.typicode.com/users"

resposta = requests.get(url)
dados = resposta.json()


primeiro_usuario = dados[0]
print(primeiro_usuario['address']['city'])