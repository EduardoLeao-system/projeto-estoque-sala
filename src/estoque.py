class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, nome , preco, quantidade):
        if nome in self.produtos:
          self.produtos[nome]["quantidade"] += int(quantidade)
        else:
         self.produtos[nome] = {"preco": float(preco),
                                "quantidade": int(quantidade)}
    def remover_produto(self, nome, quantidade):
        if nome not in self.produtos:
            raise ValueError("Produtos nao encontrado")
        if self.produtos[nome]["quantidade"]< int(quantidade):
            raise ValueError("Estoque Insuficiente")
        self.produtos[nome]["quantidade"]-= int(quantidade)
    
    
    def consultar_produto(self, nome):
        return self.produtos.get(nome)

    def disponivel(self, nome,quantidade):
        dados =self.consultar_produto(nome)
        return bool(dados and dados["quantidadee"]>= quantidade)
    def valor_total(self):
        total = 0.0
        for dados in self.produtos.values():
            total += float(dados["preco"]) * int(dados["quantidade"])
        return total   
        