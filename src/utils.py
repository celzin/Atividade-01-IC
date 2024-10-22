# utils.py
import numpy as np

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
