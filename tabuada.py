#! /usr/bin/env python3
"""Imprime a tabuada do 1 a 10.
Exemplo da impressao das tabuadas:
---Tabuada do 1---
    1 x 1 = 1
    1 x 2 = 2
    1 x 3 = 3
...
##################
---Tabuada do 2---
    2 x 1 = 2
    2 x 2 = 4
...
"""
__versao__ = "0.1.1"
__autor__ = "Thais Bueno"

numeros_tabuada = list(range(1, 11))

for tabuada in numeros_tabuada:
    print("{:-^18}".format(f"Tabuada do {tabuada}"))
    print()
    for multiplicador in numeros_tabuada:
        resultado = tabuada * multiplicador
        print("{:^18}".format(f"{tabuada} x {multiplicador} = {resultado}"))
    print()
    print("#" * 18)