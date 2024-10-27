import numpy as np
from relations import fuzzy_relation_binaria, tnorm_diferenca_limitada, tnorm_min, s_norma_soma_probabilistica, s_norma_soma_limitada
from utils import plot_heatmap, plot_comparison_membership

def executar_etapa4():
    # Definir o domínio das alturas e idades conforme o exemplo
    dominio_altura = np.array([1.60, 1.65, 1.70, 1.75, 1.80, 1.85, 1.90])
    dominio_idade = np.array([25, 30, 35, 40, 45, 50, 55])

    # Graus de pertinência para o conjunto ALTO (Altura)
    altura_values = [0, 1, 1, 1, 1, 0, 0]

    # Graus de pertinência para o conjunto MEIA-IDADE (Idade)
    idade_values = [0, 1, 1, 1, 1, 0, 0]

    # Plotar os gráficos de pertinência
    plot_comparison_membership(dominio_altura, altura_values, dominio_idade, idade_values)

    # Comparação entre T-Normas

    # 1. Relação fuzzy usando a t-norma de Diferença Limitada
    relation_binaria_diferenca = fuzzy_relation_binaria(tnorm_diferenca_limitada, altura_values, idade_values)
    print("Relação Binária Fuzzy (Diferença Limitada - T-norma):")
    for row in relation_binaria_diferenca:
        print([f"{value:.2f}" for value in row])
    plot_heatmap(relation_binaria_diferenca, "Diferença Limitada - T-norma")

    # 2. Relação fuzzy usando a t-norma de Interseção Mínima
    relation_binaria_min = fuzzy_relation_binaria(tnorm_min, altura_values, idade_values)
    print("\nRelação Binária Fuzzy (Interseção Mínima - T-norma):")
    for row in relation_binaria_min:
        print([f"{value:.2f}" for value in row])
    plot_heatmap(relation_binaria_min, "Interseção Mínima - T-norma")

    # Comparação entre S-Normas

    # 1. Relação fuzzy usando a s-norma de Soma Probabilística
    relation_binaria_soma_prob = fuzzy_relation_binaria(s_norma_soma_probabilistica, altura_values, idade_values)
    print("\nRelação Binária Fuzzy (Soma Probabilística - S-norma):")
    for row in relation_binaria_soma_prob:
        print([f"{value:.2f}" for value in row])
    plot_heatmap(relation_binaria_soma_prob, "Soma Probabilística - S-norma")

    # 2. Relação fuzzy usando a s-norma de Soma Limitada
    relation_binaria_soma_limitada = fuzzy_relation_binaria(s_norma_soma_limitada, altura_values, idade_values)
    print("\nRelação Binária Fuzzy (Soma Limitada - S-norma):")
    for row in relation_binaria_soma_limitada:
        print([f"{value:.2f}" for value in row])
    plot_heatmap(relation_binaria_soma_limitada, "Soma Limitada - S-norma")
