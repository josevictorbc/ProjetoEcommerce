from requisitos.consultar_produto import consultar_produto
from models import Produto

def test_consultar_produto():
    produto = consultar_produto("Modelo")
    assert produto is not None
    assert isinstance(produto, Produto)
    assert produto.modelo == "Modelo"
