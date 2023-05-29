from pydantic import BaseModel

# Criando a classe produto
class Produto(BaseModel):
    modelo: str
    marca: str
    ano: int
    cor: str
    preco: float
    quantidade: int
