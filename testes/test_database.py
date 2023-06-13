from database import conexao

# Teste de Conexão
def status():
    teste_conexao = conexao().status
    assert teste_conexao == 1
