#! /usr/bin/env python3
"""Exibe relatório de crianças por atividade.
Imprimir a lista de crianças agrupadas por turma que frequantam
cada uma das atividade.
"""
__versao__ = "0.1.0"
__autor__ = "Thais Bueno"

#Dados
turma1 = ["Chaves", "Chiquinha", "Quico", "Ñoño"]
turma2 = ["Godínez","Paty","Popis"]

aula_aritmetica = ["Quico", "Ñoño","Popis"]
aula_musica = ["Chaves", "Chiquinha","Godínez","Paty","Popis"]
aula_ingles = ["Chaves", "Chiquinha", "Quico", "Ñoño","Paty","Godínez"]

atividades = [
    ("Aritmética", aula_aritmetica),
    ("Música", aula_musica), 
    ("Inglês", aula_ingles),
]

# Listar alunos em cada atividade por sala
for nome_atividade, atividade in atividades:
    print(f"Alunos da Atividade {nome_atividade}\n")

    atividade_turma1=set(turma1) & set(atividade)
    atividade_turma2=set(turma2) & set(atividade)

    print("Turma 01: ", atividade_turma1)
    print("Turma 02: ", atividade_turma2)
    print("-" * 50)
