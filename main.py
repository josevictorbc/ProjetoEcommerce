from fastapi import FastAPI
from models import Produto
from requisitos.adicionar_produto import adicionar_produto
from requisitos.deletar_produto import deletar_produto
from requisitos.update_produto import update_produto
from requisitos.listar_produtos import listar_produtos
from requisitos.consultar_produto import consultar_produto

app = FastAPI()

@app.post("/produtos")
def criar_produto(produto: Produto):
    resultado = adicionar_produto(produto)
    return resultado

@app.delete("/produtos/{modelo}")
def remover_produto(modelo: str):
    resultado = deletar_produto(modelo)
    return resultado

@app.put("/produtos")
def atualizar_produto(produto: Produto):
    resultado = update_produto(produto)
    return resultado

@app.get("/produtos")
def listar_todos_produtos():
    produtos = listar_produtos()
    return produtos

@app.get("/produtos/{modelo}")
def consultar_produto(modelo: str):
    produto = consultar_produto(modelo)
    if produto is None:
        return {"mensagem": "Produto não encontrado"}
    return produto
