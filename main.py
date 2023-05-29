from fastapi import FastAPI
from models import Produto
from database import conexao

app = FastAPI()

@app.post("/produtos")
def adicionar_produto(produto: Produto):
    # Verifica se o ano, o preço e a quantidade são negativos ou iguais a zero
    if produto.ano <= 0:
        raise ValueError('O ano deve ser maior que zero.')
    if produto.preco <= 0:
        raise ValueError('O preço deve ser maior que zero.')
    if produto.quantidade <= 0:
        raise ValueError('A quantidade em estoque deve ser maior que zero.')

    # Conexão com o Banco de Dados
    conn = conexao()

    try:
        cursor = conn.cursor()

        # Verifica se o produto já está cadastrado no banco
        cursor.execute("SELECT COUNT(*) FROM produto WHERE modelo = %s AND marca = %s AND cor = %s", (produto.modelo, produto.marca, produto.cor))
        produto_existe = cursor.fetchone()[0]

        if produto_existe > 0:
            raise ValueError('O produto já está cadastrado.')

        # Insere o novo produto na tabela
        query = "INSERT INTO produto (modelo, marca, ano, cor, preco, quantidade) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (produto.modelo, produto.marca, produto.ano, produto.cor, produto.preco, produto.quantidade))
        conn.commit()

    finally:
        cursor.close()
        conn.close()

    print('Produto adicionado com sucesso.')
