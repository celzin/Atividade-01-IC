import numpy as np
import matplotlib.pyplot as plt

def normalize_data(X, min_val, max_val):
    """
    Função para normalizar os dados de entrada em um intervalo [min_val, max_val].
    X: matriz de entrada
    min_val: valor mínimo do intervalo
    max_val: valor máximo do intervalo
    Retorna os dados normalizados.
    """
    X_normalized = (X - np.min(X)) / (np.max(X) - np.min(X)) * (max_val - min_val) + min_val
    return X_normalized


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