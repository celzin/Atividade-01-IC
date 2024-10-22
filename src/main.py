import numpy as np
import matplotlib.pyplot as plt
from fuzzy import triangular_mf, trapezoidal_mf, fuzzify_data
from rules import fuzzy_rule_and, fuzzy_rule_or
from utils import plot_fuzzification

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
