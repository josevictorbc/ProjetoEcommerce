from database import conexao

def deletar_produto(modelo, marca, ano, cor):
    conn = conexao()
    cursor = conn.cursor()
    query = "DELETE FROM produto WHERE modelo = %s AND marca = %s AND  ano = %s AND cor = %s"
    cursor.execute(query, (modelo, marca, ano, cor))
    conn.commit()
    cursor.close()
    conn.close()
    return {"mensagem": "Produto deletado com Sucesso"}
