import numpy as np
from relations import fuzzy_relation_binaria, tnorm_diferenca_limitada, tnorm_min
from utils import plot_comparison_membership

def executar_etapa4():
    # Definir o domínio das alturas e idades conforme o exemplo
    dominio_altura = np.array([1.60, 1.65, 1.70, 1.75, 1.80, 1.85, 1.90])
    dominio_idade = np.array([25, 30, 35, 40, 45, 50, 55])

    # Graus de pertinência para o conjunto ALTO (Altura)
    altura_values = [0, 1, 1, 1, 1, 0, 0]  # Pertinência retangular para altura

    # Graus de pertinência para o conjunto MEIA-IDADE (Idade)
    idade_values = [0, 1, 1, 1, 1, 0, 0]   # Pertinência retangular para idade

    # Plotar os gráficos de pertinência (Altura vs Idade)
    plot_comparison_membership(dominio_altura, altura_values, dominio_idade, idade_values)

    # Calcular a relação fuzzy usando a t-norma de Diferença Limitada
    relation_binaria_diferenca = fuzzy_relation_binaria(tnorm_diferenca_limitada, altura_values, idade_values)
    
    # Calcular a relação fuzzy usando a t-norma de Interseção Mínima
    relation_binaria_min = fuzzy_relation_binaria(tnorm_min, altura_values, idade_values)

    # Exibir os resultados das relações fuzzy no terminal
    print("Relação Binária Fuzzy (Diferença Limitada):")
    for row in relation_binaria_diferenca:
        print(row)

    print("\nRelação Binária Fuzzy (Interseção Mínima):")
    for row in relation_binaria_min:
        print(row)
