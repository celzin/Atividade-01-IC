import numpy as np

def triangular_mf(x, a, b, c):
    """
    Função de pertinência triangular.
    x: valor de entrada
    a: limite inferior (Mi = 0)
    b: centro (Mi = 1)
    c: limite superior (Mi = 0)
    Retorna o grau de pertinência Mi.
    """
    if x <= a or x >= c:
        return 0.0
    elif a < x <= b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)


def trapezoidal_mf(x, a, b, c, d):
    """
    Função de pertinência trapezoidal.
    a, b, c, d: limites do trapézio.
    a e d são os limites onde Mi = 0, e b e c são onde Mi = 1.
    """
    if x <= a or x >= d:
        return 0.0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x <= c:
        return 1.0
    else:
        return (d - x) / (d - c)


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