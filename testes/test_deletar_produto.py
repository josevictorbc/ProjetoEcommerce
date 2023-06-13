from requisitos.deletar_produto import deletar_produto

def test_deletar_produto():
    resultado = deletar_produto("Modelo")
    assert resultado == {"mensagem": "Produto deletado com Sucesso"}
