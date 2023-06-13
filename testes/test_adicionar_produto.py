from requisitos.adicionar_produto import adicionar_produto
from models import Produto

def test_adicionar_produto():
    produto = Produto(
        modelo="Modelo",
        marca="Marca",
        ano=2023,
        cor="Verde",
        preco=200000.00,
        quantidade=10
    )
    resultado = adicionar_produto(produto)
    assert resultado == {"mensagem": "Produto adicionado com Sucesso"}
