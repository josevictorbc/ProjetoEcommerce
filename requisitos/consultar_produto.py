from models import Produto
from database import conexao

def consultar_produto(nome):
    conn = conexao()
    cursor = conn.cursor()
    query = "SELECT * FROM produto WHERE modelo = %s"
    cursor.execute(query, (nome,))
    row = cursor.fetchone()
    if row is not None:
        produto = Produto(
            modelo=row[0],
            marca=row[1],
            ano=row[2],
            cor=row[3],
            preco=row[4],
            quantidade=row[5]
        )
        return produto
    cursor.close()
    conn.close()
    return None
