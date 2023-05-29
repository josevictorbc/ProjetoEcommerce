from database import conexao

# Teste de Conexão
def status():
    assert conexao().status == 1
