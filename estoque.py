import logging

estoque = {
    "produto_1": 10,
    "produto_2": 0, 
}

def verificar_estoque(produto_id, quantidade):
    return estoque.get(produto_id, 0) >= quantidade



def cadastrar_produto(nome, preco, quantidade):
  
    estoque[nome] = {"preco": preco, "quantidade": quantidade}


def test_cadastrar_produto():
    estoque.clear()
    cadastrar_produto("Produto A", 10.0, 5)
    assert "Produto A" in estoque
    assert estoque["Produto A"]["preco"] == 10.0
    assert estoque["Produto A"]["quantidade"] == 5

