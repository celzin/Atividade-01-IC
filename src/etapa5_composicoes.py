import numpy as np
from compositions import fuzzy_composition_max_min, fuzzy_composition_min_max, fuzzy_composition_max_prod
from utils import plot_fuzzy_compositions

def executar_etapa5():
    # Definir os domínios de altura e idade diretamente como listas
    dominio_altura = [1.60, 1.65, 1.70, 1.75, 1.80, 1.85, 1.90]
    dominio_idade = [25, 30, 35, 40, 45, 50, 55]

    # Graus de pertinência para o conjunto ALTO (Altura)
    altura_values = [0, 1, 1, 1, 1, 0, 0]

    # Graus de pertinência para o conjunto MEIA-IDADE (Idade)
    idade_values = [0, 1, 1, 1, 1, 0, 0]

    # Converter as listas de valores em matrizes manuais (listas de listas)
    matriz_altura = [[value] for value in altura_values]  # Matriz coluna
    matriz_idade = [idade_values]  # Matriz linha

    # Aplicando as composições fuzzy (Max-Min, Min-Max, Max-Prod)
    matrix_max_min = fuzzy_composition_max_min(matriz_altura, matriz_idade)
    matrix_min_max = fuzzy_composition_min_max(matriz_altura, matriz_idade)
    matrix_max_prod = fuzzy_composition_max_prod(matriz_altura, matriz_idade)

    # Exibir as matrizes no terminal
    print("Matriz Max-Min:")
    for row in matrix_max_min:
        print([f"{value:.2f}" for value in row])

    print("\nMatriz Min-Max:")
    for row in matrix_min_max:
        print([f"{value:.2f}" for value in row])

    print("\nMatriz Max-Prod:")
    for row in matrix_max_prod:
        print([f"{value:.2f}" for value in row])

    # Gerar a visualização gráfica comparativa das composições fuzzy
    plot_fuzzy_compositions(matrix_max_min, matrix_min_max, matrix_max_prod)