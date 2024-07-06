#! /usr/bin/env python3
"""Hello Word Multi Linguas.

Dependendo da linha configurada no ambiente o programa exibe a mensagem 
correspondente.

Como Usar:
Tenha a variavél LANG devidamente configurada ex:

    export LANG=pt_BR
    
Execução:
    python3 hello.py
    ou
    ./hello.py
"""
__versao__ = "0.0.1"
__autor__ = "Thais Bueno"
__licenca__ = "Unlicence"

import os

linguagem_atual = os.getenv("LANG","en_US")[:5]
mensagem = "Hello, Word!"

if linguagem_atual == "pt_BR":
    mensagem = "Olá, Mundo!"
elif linguagem_atual == "it_IT":
    mensagem = "Ciao, Mondo!"    
elif linguagem_atual == "es_SP":
    mensagem = "Hola, Mundo!"  
elif linguagem_atual == "de_DE":
    mensagem = "Hallo Welt!"  
elif linguagem_atual == "fr_FR":
    mensagem = "Bonjour le monde!"  

print(mensagem)