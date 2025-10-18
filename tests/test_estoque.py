import pytest
from src.estoque import Estoque

@pytest.mark.estoque
def test_adicionar_produto_simples():
    e = Estoque()
    e.adicionar_produto("Arroz", 10.0, 5)
    assert e.consultar_produto("Arroz") == {"preco": 10.0, "quantidade":5}

@pytest.mark.estoque
def test_reAdicionar_soma_quantidade_mantem_preco():
    e = Estoque()
    e.adicionar_produto("Arroz", 10.0, 5)
    e.adicionar_produto("Arroz", 90.0, 3)
    assert e.consultar_produto("Arroz") == {"preco": 10.0, "quantidade": 8}

@pytest.mark.estoque
def test_remover_produto_sucesso():
    e = Estoque()
    e.adicionar_produto("Feijao":)