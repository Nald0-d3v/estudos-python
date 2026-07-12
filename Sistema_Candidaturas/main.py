import sqlite3
from datetime import datetime


# Criar banco e tabela

def criar_tabela():
    conexao = sqlite3.connect("candidaturas.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS candidaturas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            empresa TEXT,
            cargo TEXT,
            salario REAL,
            modalidade TEXT,
            status TEXT,
            data TEXT
        )
    """)

    conexao.commit()
    conexao.close()


# Adicionar candidatura

def adicionar_candidatura():
    empresa = input("Nome da empresa: ").strip()
    cargo = input("Nome do cargo: ").strip()

    while True:
        try:
            salario = float(input("Salário: "))

            if salario < 0:
                print("O salário não pode ser negativo.")
                continue

            break

        except ValueError:
            print("Digite um salário válido usando números.")

    modalidade = input("Modalidade: ").strip()
    status = input("Status atual: ").strip().lower()

    while True:
        data = input("Digite a data (DD/MM/AAAA): ")

        try:
            data_validada = datetime.strptime(data, "%d/%m/%Y")

            # Converte novamente para texto antes de salvar
            data = data_validada.strftime("%d/%m/%Y")
            break

        except ValueError:
            print("Data inválida.")

    conexao = sqlite3.connect("candidaturas.db")
    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO candidaturas (
            empresa,
            cargo,
            salario,
            modalidade,
            status,
            data
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            empresa,
            cargo,
            salario,
            modalidade,
            status,
            data
        )
    )

    conexao.commit()
    conexao.close()

    print("Candidatura adicionada com sucesso.")


# Listar candidaturas

def listar_candidaturas():
    conexao = sqlite3.connect("candidaturas.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM candidaturas")
    candidaturas = cursor.fetchall()

    if not candidaturas:
        print("Nenhuma candidatura cadastrada.")

    else:
        print("\nCandidaturas cadastradas:\n")

        for candidatura in candidaturas:
            print("ID:", candidatura[0])
            print("Empresa:", candidatura[1])
            print("Cargo:", candidatura[2])
            print("Salário:", candidatura[3])
            print("Modalidade:", candidatura[4])
            print("Status:", candidatura[5])
            print("Data:", candidatura[6])
            print("-" * 30)

    conexao.close()


# Atualizar status

def atualizar_status():
    conexao = sqlite3.connect("candidaturas.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM candidaturas")
    candidaturas = cursor.fetchall()

    if not candidaturas:
        print("Nenhuma candidatura cadastrada.")
        conexao.close()
        return

    for candidatura in candidaturas:
        print(
            "Empresa:",
            candidatura[1],
            "- ID:",
            candidatura[0]
        )

    status_validos = [
        "enviado",
        "em análise",
        "entrevista",
        "recusado",
        "contratado"
    ]

    print("\nStatus disponíveis:")

    for status in status_validos:
        print("-", status)

    while True:
        identificar = input(
            "\nDigite o ID da candidatura que deseja alterar: "
        )

        novo_status = input(
            "Digite o novo status: "
        ).strip().lower()

        if novo_status not in status_validos:
            print("Status inválido.")
            continue

        cursor.execute(
            "UPDATE candidaturas SET status = ? WHERE id = ?",
            (novo_status, identificar)
        )

        conexao.commit()
        conexao.close()

        print("Status atualizado com sucesso.")
        break


# Remover candidatura

def remover_candidatura():
    conexao = sqlite3.connect("candidaturas.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM candidaturas")
    candidaturas = cursor.fetchall()

    if not candidaturas:
        print("Nenhuma candidatura cadastrada.")
        conexao.close()
        return

    for candidatura in candidaturas:
        print(
            "Empresa:",
            candidatura[1],
            "- ID:",
            candidatura[0]
        )

    identificar = input(
        "Digite o ID da candidatura que deseja excluir: "
    )

    cursor.execute(
        "DELETE FROM candidaturas WHERE id = ?",
        (identificar,)
    )

    conexao.commit()
    conexao.close()

    print("Candidatura excluída com sucesso.")


# Início do programa

criar_tabela()

print("\nSistema de candidaturas")
print("Comandos disponíveis:")
print("- adicionar candidatura")
print("- listar candidaturas")
print("- atualizar status")
print("- remover candidatura")
print("- sair")

while True:
    menu = input("\nComando: ").strip().lower()

    if menu == "sair":
        print("Encerrando programa.")
        break

    elif menu == "adicionar candidatura":
        adicionar_candidatura()

    elif menu == "listar candidaturas":
        listar_candidaturas()

    elif menu == "atualizar status":
        atualizar_status()

    elif menu == "remover candidatura":
        remover_candidatura()

    else:
        print("Comando inválido.")