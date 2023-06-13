from requisitos.update_produto import update_produto
from models import Produto

def test_update_produto():
    produto = Produto(
        modelo="Modelo",
        marca="Marca",
        ano=2023,
        cor="Azul",
        preco=390000.00,
        quantidade=5
    )
    resultado = update_produto(produto)
    assert resultado == {"mensagem": "Produto atualizado com Sucesso"}
