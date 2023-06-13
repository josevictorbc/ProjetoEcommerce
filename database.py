import psycopg2

def conexao():
    return psycopg2.connect(
        database="postgres",
        host = "localhost",
        user="postgres",
        password="ja@2023",
        port = "5432"
    )
