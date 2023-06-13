from models import Produto
from database import conexao

def adicionar_produto(produto: Produto):
    conn = conexao()
    cursor = conn.cursor()
    query = "INSERT INTO produto (modelo, marca, ano, cor, preco, quantidade) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (produto.modelo, produto.marca, produto.ano, produto.cor, produto.preco, produto.quantidade))
    conn.commit()
    cursor.close()
    conn.close()
    return {"mensagem": "Produto adicionado com Sucesso"}
