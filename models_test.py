from models import Produto

def test_constructor():
    produto = Produto(modelo='modelo', marca='marca', ano=2003, cor='cor', preco=10, quantidade=1)
    assert produto.modelo == 'modelo'
    assert produto.marca == 'marca'
    assert produto.ano == 2003
    assert produto.cor == 'cor'
    assert produto.preco == 10
    assert produto.quantidade == 1
