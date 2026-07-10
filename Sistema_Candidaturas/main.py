import sqlite3


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


def adicionar_candidatura():

    empresa = input("Nome da empresa: ")
    cargo = input("Nome do cargo: ")
    salario = int(input("Salario: "))
    modalidade = input("Modalidade: ")
    status = input("Status atual: ")
    data = input("Data: ")


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


def listar_candidaturas():
    conexao = sqlite3.connect("candidaturas.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM candidaturas")
    candidatos = cursor.fetchall()

    if not candidatos:
        print("Nenhuma candidatura cadastrada.")
    else:
        print("\nCandidaturas cadastradas:\n")

        for candidato in candidatos:
            print("ID:", candidato[0])
            print("Empresa:", candidato[1])
            print("Cargo:", candidato[2])
            print("Salário:", candidato[3])
            print("Modalidade:", candidato[4])
            print("Status:", candidato[5])
            print("Data:", candidato[6])
            print("-" * 30)

    conexao.close()


def atualizar_status():
    conexao = sqlite3.connect("candidaturas.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM candidaturas")
    candidatos = cursor.fetchall()

    if not candidatos:
        print("Nenhuma candidatura cadastrada.")
        conexao.close()
        return

    for candidato in candidatos:
        print("Empresa:", candidato[1], "- ID:", candidato[0])


    status_validos = [
    "enviado",
    "em análise",
    "entrevista",
    "recusado",
    "contratado"
        ]

    print()
    print("Status disponiveis: ")
    print("enviado")
    print("em análise")
    print("entrevista")
    print("recusado")
    print("contratado")
    print()

    while True:

        identificar = input("Digite o ID da empresa que deseja mudar: ")
        novo_status = input("Digite o status desejado: ")

        if novo_status not in status_validos:
            print("Status invalido")
            continue

        cursor.execute(
            "UPDATE candidaturas SET status = ? WHERE id = ?",
            (novo_status, identificar)
        )

        conexao.commit()
        conexao.close()

        print("Status atualizado com sucesso.")
        break


def remover_candidatura():
    conexao = sqlite3.connect("candidaturas.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM candidaturas")
    candidatos = cursor.fetchall()

    if not candidatos:
        print("Nenhuma candidatura cadastrada.")
        conexao.close()
        return

    for candidato in candidatos:
        print("Empresa:", candidato[1], "- ID:", candidato[0])

    identificar = input("Digite o ID da empresa que deseja exluir: ")

    cursor.execute(
    "DELETE FROM candidaturas WHERE id = ?",
    (identificar,))

    conexao.commit()
    conexao.close()

    print("Empresa excluida com sucesso.")

    #entao remover seria assim?


criar_tabela()

while True:
    menu = input("Comando: ").strip().lower()


    if menu == 'sair':
        print("Encerrando programa.")
        break

    elif menu == 'atualizar status':

        atualizar_status()

    elif menu == 'adicionar candidatura':

        adicionar_candidatura()

    elif menu == 'remover candidatura':
        
        remover_candidatura()

    elif menu == 'listar candidatura':

        listar_candidaturas() 