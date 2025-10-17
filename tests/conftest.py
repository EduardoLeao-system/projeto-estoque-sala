import pytest
from src.estoque import Estoque

@pytest.fixture
def estoque_vazio():
    return Estoque()

@pytest.fixture
def estoque_com_itens():
    e = Estoque()
    e.adicionar_produto("Arroz", 10.0, 5)
    e.adicionar_produto("Leite", 6.0, 2)
    return e