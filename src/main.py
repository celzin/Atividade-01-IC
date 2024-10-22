# main.py
import numpy as np
import matplotlib.pyplot as plt
from fuzzy import triangular_mf, trapezoidal_mf
from rules import fuzzy_rule_and, fuzzy_rule_or


def fuzzify_data(X, a, b, c):
    """
    Função para fuzzificar um conjunto de dados de entrada usando uma função de pertinência triangular.
    X: Matriz de dados de entrada (M x N)
    a, b, c: Parâmetros da função triangular
    Retorna uma matriz de graus de pertinência.
    """
    M, N = X.shape
    Mi = np.zeros((M, N))  # Matriz para armazenar os graus de pertinência
    for i in range(M):
        for j in range(N):
            Mi[i][j] = triangular_mf(X[i][j], a, b, c)
    return Mi


def plot_fuzzification(X, Mi):
    """
    Função para plotar os resultados da fuzzificação.
    X: Matriz de entrada original.
    Mi: Matriz de graus de pertinência (fuzzificada).
    """
    for i in range(len(X)):
        plt.plot(X[i], Mi[i], label=f'Conjunto {i+1}')
    
    plt.title('Fuzzificação dos Conjuntos de Dados')
    plt.xlabel('Valores de Entrada')
    plt.ylabel('Grau de Pertinência')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # Exemplo de dados de entrada (M x N)
    X = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
    a, b, c = 0, 5, 10  # Parâmetros da função triangular

    # Fuzzificar os dados usando a função triangular
    Mi = fuzzify_data(X, a, b, c)
    
    # Plotar os resultados da fuzzificação
    plot_fuzzification(X, Mi)

    # Aplicar regras fuzzy (exemplos)
    regra_and = fuzzy_rule_and(Mi[0][1], Mi[1][1])
    regra_or = fuzzy_rule_or(Mi[0][2], Mi[2][2])
    
    print(f'Resultado da Regra "E" (AND): {regra_and}')
    print(f'Resultado da Regra "OU" (OR): {regra_or}')
