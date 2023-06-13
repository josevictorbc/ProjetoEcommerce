from models import Produto
from database import conexao

def update_produto(produto: Produto):
    conn = conexao()
    cursor = conn.cursor()
    query = "UPDATE produto SET preco = %s, quantidade = %s WHERE modelo = %s"
    cursor.execute(query, (produto.preco, produto.quantidade, produto.modelo))
    conn.commit()
    cursor.close()
    conn.close()
    return {"mensagem": "Produto atualizado com Sucesso"}
