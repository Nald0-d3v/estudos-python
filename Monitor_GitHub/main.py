import sqlite3
from datetime import datetime

import requests


# Exibir comandos

def mostrar_comandos():
    print("\nComandos disponíveis:")
    print("1 - Consultar e salvar usuário")
    print("2 - Remover usuário")
    print("3 - Listar usuários")
    print("4 - Ajuda")
    print("0 - Sair")


# Criar banco e tabela

def criar_tabela():
    conexao = sqlite3.connect("github.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT,
            seguidores INTEGER,
            seguindo INTEGER,
            repositorios INTEGER,
            data_criacao TEXT,
            data_consulta TEXT
        )
    """)

    conexao.commit()
    conexao.close()


# Consultar usuário na API do GitHub

def consultar_usuario():
    while True:
        usuario = input(
            "\nDigite o nome do usuário ou 'voltar': "
        ).strip().lower()

        if usuario == "voltar":
            return None

        if not usuario:
            print("O nome do usuário não pode ficar vazio.")
            continue

        url = "https://api.github.com/users/" + usuario

        try:
            resposta = requests.get(url, timeout=10)

        except requests.RequestException:
            print("Não foi possível conectar à API do GitHub.")
            return None

        if resposta.status_code == 404:
            print("Usuário não encontrado.")
            continue

        if resposta.status_code != 200:
            print("A consulta apresentou um erro.")
            return None

        dados = resposta.json()

        print()
        print("Usuário:", dados["login"])
        print("Seguidores:", dados["followers"])
        print("Seguindo:", dados["following"])
        print("Repositórios públicos:", dados["public_repos"])
        print("Conta criada em:", dados["created_at"])
        print()

        return dados


# Salvar usuário no banco

def salvar_usuario(dados):
    conexao = sqlite3.connect("github.db")
    cursor = conexao.cursor()

    login = dados["login"]
    seguidores = dados["followers"]
    seguindo = dados["following"]
    repositorios = dados["public_repos"]
    data_criacao = dados["created_at"]

    data_consulta = datetime.now().strftime("%d/%m/%Y %H:%M")

    cursor.execute(
        "SELECT id FROM usuarios WHERE login = ?",
        (login,)
    )

    resultado = cursor.fetchone()

    if resultado is not None:
        print("Esse usuário já foi consultado e salvo.")

    else:
        cursor.execute(
            """
            INSERT INTO usuarios (
                login,
                seguidores,
                seguindo,
                repositorios,
                data_criacao,
                data_consulta
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                login,
                seguidores,
                seguindo,
                repositorios,
                data_criacao,
                data_consulta
            )
        )

        print("Usuário salvo com sucesso.")

    conexao.commit()
    conexao.close()


# Listar usuários salvos

def listar_usuarios():
    conexao = sqlite3.connect("github.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    if not usuarios:
        print("Nenhum usuário salvo.")

    else:
        print("\nUsuários salvos:\n")

        for usuario in usuarios:
            print("ID:", usuario[0])
            print("Login:", usuario[1])
            print("Seguidores:", usuario[2])
            print("Seguindo:", usuario[3])
            print("Repositórios:", usuario[4])
            print("Data de criação:", usuario[5])
            print("Data da consulta:", usuario[6])
            print("-" * 30)

    conexao.close()


# Remover usuário

def remover_usuario():
    conexao = sqlite3.connect("github.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT id, login FROM usuarios")
    usuarios = cursor.fetchall()

    if not usuarios:
        print("Nenhum usuário salvo.")
        conexao.close()
        return

    print("\nUsuários disponíveis:\n")

    for usuario in usuarios:
        print("Login:", usuario[1], "- ID:", usuario[0])

    identificar = input(
        "\nDigite o ID do usuário que deseja remover: "
    ).strip()

    if not identificar.isdigit():
        print("Digite um ID válido usando números.")
        conexao.close()
        return

    cursor.execute(
        "DELETE FROM usuarios WHERE id = ?",
        (identificar,)
    )

    if cursor.rowcount == 0:
        print("ID não encontrado.")

    else:
        conexao.commit()
        print("Usuário excluído com sucesso.")

    conexao.close()


# Início do programa

criar_tabela()

print("Bem-vindo ao monitor de usuários do GitHub.")
mostrar_comandos()

while True:
    try:
        menu = int(input("\nComando: "))

    except ValueError:
        print("Digite um comando válido usando números.")
        continue

    if menu == 0:
        print("Programa encerrado.")
        break

    elif menu == 1:
        dados = consultar_usuario()

        if dados is not None:
            salvar_usuario(dados)

    elif menu == 2:
        remover_usuario()

    elif menu == 3:
        listar_usuarios()

    elif menu == 4:
        mostrar_comandos()

    else:
        print("Comando inválido.")