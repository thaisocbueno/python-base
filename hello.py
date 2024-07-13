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
__versao__ = "0.1.3"
__autor__ = "Thais Bueno"
__licenca__ = "Unlicence"

import os

current_language = os.getenv("LANG","en_US")[:5]

message = {
    "en_US": "Hello, Word!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "de_DE": "Hallo Welt!",
    "fr_FR": "Bonjour le monde!"
}

print(message[current_language])