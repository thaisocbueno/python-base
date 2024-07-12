#! /usr/bin/env python3
"""Exibe relatório de crianças por atividade.
Imprimir a lista de crianças agrupadas por turma que frequantam
cada uma das atividade.
"""
__versao__ = "0.1.0"
__autor__ = "Thais Bueno"

#Dados
turmas = {
    "Turma 01": ["Chaves", "Chiquinha", "Quico", "Ñoño"],
    "Turma 02": ["Godínez","Paty","Popis"]
}

atividades = {
    "Aritmetica": ["Quico", "Ñoño","Popis"],
    "Musica": ["Chaves", "Chiquinha","Godínez","Paty","Popis"],
    "Ingles": ["Chaves", "Chiquinha", "Quico", "Ñoño","Paty","Godínez"]
}

# Listar alunos em cada atividade por sala
for atividade, alunos in atividades.items():
    print(f"Alunos da Atividade {atividade}\n")
    
    atividade_turma1=[]
    atividade_turma2=[]
    
    for aluno in alunos:
        if aluno in turmas["Turma 01"]:
            atividade_turma1.append(aluno)
        elif aluno in turmas["Turma 02"]:
            atividade_turma2.append(aluno)
            
    print("Turma 01: ", atividade_turma1)
    print("Turma 02: ", atividade_turma2)
    print("-" * 50)