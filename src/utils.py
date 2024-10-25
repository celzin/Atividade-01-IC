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


def plot_fuzzification(X, Mi, function_name):
    """
    Função para plotar os resultados da fuzzificação.
    X: Matriz de entrada original.
    Mi: Matriz de graus de pertinência (fuzzificada).
    function_name: Nome da função de pertinência sendo plotada.
    """
    for i in range(len(X)):
        plt.plot(X[i], Mi[i], label=f'Conjunto {i+1}')
    
    plt.title(f'Fuzzificação dos Conjuntos de Dados - {function_name}')
    plt.xlabel('Valores de Entrada')
    plt.ylabel('Grau de Pertinência')
    plt.legend()
    plt.show()


def plot_fuzzification_overlay(X, Mis, function_name):
    """
    Função para plotar os resultados da fuzzificação com sobreposição de funções.
    X: Matriz de entrada original.
    Mis: Lista de matrizes de graus de pertinência (fuzzificadas).
    function_name: Nome da função de pertinência sendo plotada.
    """
    for i, Mi in enumerate(Mis):
        plt.plot(X[0], Mi[0], label=f'Conjunto {i+1}')
    
    plt.title(f'Fuzzificação dos Conjuntos - Sobreposição ({function_name})')
    plt.xlabel('Valores de Entrada')
    plt.ylabel('Grau de Pertinência')
    plt.legend()
    plt.show()
