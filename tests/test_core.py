import pytest
from core import calcular_total, processar_pedido
from estoque import cadastrar_produto, estoque
from core import finalizar_pedido


def test_calcular_total_sem_desconto():
    assert calcular_total(10, 2) == 20

def test_calcular_total_com_desconto():
    assert calcular_total(10, 2, desconto=0.1) == 18

def test_calcular_total_parametros_invalidos():
    with pytest.raises(ValueError):
        calcular_total(-5, 2)

def test_processar_pedido_sucesso():
    total = processar_pedido("produto_1", 2, 15)
    assert total == 30

def test_processar_pedido_estoque_insuficiente():
    with pytest.raises(RuntimeError):
        processar_pedido("produto_2", 1, 10)
def test_cadastrar_produto():
    estoque.clear()
    cadastrar_produto("Produto A", 10.0, 5)
    assert "Produto A" in estoque
    assert estoque["Produto A"]["preco"] == 10.0
    assert estoque["Produto A"]["quantidade"] == 5

def test_finalizar_pedido():
    pedido = [
        {"nome": "Produto A", "preco": 10.0, "quantidade": 2},
        {"nome": "Produto B", "preco": 5.0, "quantidade": 3}
    ]
    total = finalizar_pedido(pedido)
    assert total == 10.0 * 2 + 5.0 * 3