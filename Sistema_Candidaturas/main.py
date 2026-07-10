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


def adicionar_candidatura(
    empresa,
    cargo,
    salario,
    modalidade,
    status,
    data
):
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


criar_tabela()

# adicionar_candidatura(
#     "Google",
#     "Analista",
#     2500,
#     "Remoto",
#     "Enviado",
#     "09/07/2026"
# )

listar_candidaturas()