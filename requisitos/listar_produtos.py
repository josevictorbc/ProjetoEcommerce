from models import Produto
from database import conexao

def listar_produtos():
    conn = conexao()
    cursor = conn.cursor()
    query = "SELECT * FROM produto"
    cursor.execute(query)
    produtos = []
    for row in cursor:
        produto = Produto(
            modelo=row[0],
            marca=row[1],
            ano=row[2],
            cor=row[3],
            preco=row[4],
            quantidade=row[5]
        )
        produtos.append(produto)
    cursor.close()
    conn.close()
    return produtos
