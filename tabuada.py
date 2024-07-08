#! /usr/bin/env python3
"""Imprime a tabuada do 1 a 10."""
__versao__ = "0.0.1"
__autor__ = "Thais Bueno"

#Range inicia no 0
numeros_tabuada = list(range(0, 11))

for numero_tabuada in numeros_tabuada:
    print("Tabuada do: ", numero_tabuada)
    for numero_multiplicado in numeros_tabuada:
        resultado = numero_tabuada * numeros_tabuada[numero_multiplicado]
        print(numero_tabuada, " x ", numeros_tabuada[numero_multiplicado], 
              " = ", resultado)
    print("-" * 12)