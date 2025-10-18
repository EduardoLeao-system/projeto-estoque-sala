import pytest
from src.estoque import Estoque

@pytest.mark.estoque
def test_adicionar_produto_simples():
    e = Estoque()
    e.adicionar_produto("Arroz", 10.0, 5)
    assert e.consultar_produto("Arroz") == {"preco": 10.0, "quantidade":5}