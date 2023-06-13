from requisitos.listar_produtos import listar_produtos

def test_listar_produtos():
    produtos = listar_produtos()
    assert len(produtos) > 0
