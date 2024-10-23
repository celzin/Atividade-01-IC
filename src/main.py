import numpy as np
from fuzzy import fuzzify_data
from rules import fuzzy_rule_and, fuzzy_rule_or
from utils import plot_fuzzification

if __name__ == "__main__":
    # Exemplo de dados de entrada (M x N)
    X = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
    a, b, c = 0, 5, 10  # Parâmetros da função triangular

    # Fuzzificar os dados usando a função triangular
    Mi = fuzzify_data(X, a, b, c)
    
    print("Matriz de graus de pertinência (Mi):")
    for row in Mi:
        print([f"{value:.2f}" for value in row])

    plot_fuzzification(X, Mi)

    regra_and = fuzzy_rule_and(Mi[0][1], Mi[1][1])  # Exemplo entre Mi[0][1] e Mi[1][1]
    print(f"Regra AND para Mi[0][1] e Mi[1][1]: {regra_and}")

    regra_or = fuzzy_rule_or(Mi[0][2], Mi[2][2])  # Exemplo entre Mi[0][2] e Mi[2][2]
    print(f"Regra OR para Mi[0][2] e Mi[2][2]: {regra_or}")
