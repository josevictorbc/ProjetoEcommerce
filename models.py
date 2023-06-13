from pydantic import BaseModel

class Produto(BaseModel):
    modelo: str
    marca: str
    ano: int
    cor: str
    preco: float
    quantidade: int
