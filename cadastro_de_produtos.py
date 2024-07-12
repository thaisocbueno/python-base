#! /usr/bin/env python3
"""Cadastro de Produto
"""
__versao__ = "0.1.0"
__autor__ = "Thais Bueno"

from pprint import pprint

produto = {
    "nome": "caneta",
    "cores": ["azul","branco"],
    "preco": 3.23,
    "dimensao": {
        "altura": 12.1,
        "largura": 0.8
    },
    "em_estoque": True,
    "codigo": 45678,
    "codebar": None,
}

cliente = {
    "nome": "Thais"
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3
}

#pprint(compra)

total_compra = compra["quantidade"] * compra["produto"]["preco"]

print(
    f"Cliente {compra['cliente']['nome']}"
    f" comprou {compra['quantidade']} unidades de {compra['produto']['nome']}"
    f" e pagou o total de {total_compra}"
)

