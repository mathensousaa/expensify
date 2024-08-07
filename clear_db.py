import sqlite3


def clear_database(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Obtém a lista de tabelas no banco de dados
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]
        print(f"Excluindo dados da tabela: {table_name}")
        cursor.execute(f"DELETE FROM {table_name}")

    conn.commit()
    conn.close()
    print("Banco de dados limpo com sucesso!")


if __name__ == "__main__":
    DB_PATH = "expensify.db"  # Caminho para o seu banco de dados
    clear_database(DB_PATH)
