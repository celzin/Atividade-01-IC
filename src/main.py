import numpy as np
from fuzzy import (fuzzify_triangular, fuzzify_trapezoidal, fuzzify_gaussian, fuzzify_sigmoidal, 
                   fuzzify_bell, fuzzify_s_shaped, fuzzify_z_shaped, fuzzify_cauchy, 
                   fuzzify_double_gaussian, fuzzify_linear_piecewise, fuzzify_polynomial)
from utils import plot_fuzzification

if __name__ == "__main__":
    # Exemplo de dados de entrada (M x N)
    X = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])

    # Testando a função triangular
    a, b, c = 0, 5, 10  # Parâmetros da função triangular
    Mi_triangular = fuzzify_triangular(X, a, b, c)
    print("Triangular: Matriz de graus de pertinência:")
    for row in Mi_triangular:
        print([f"{value:.2f}" for value in row])
    plot_fuzzification(X, Mi_triangular, "Triangular")

    # Testando a função trapezoidal
    a, b, c, d = 0, 3, 7, 10  # Parâmetros da função trapezoidal
    Mi_trapezoidal = fuzzify_trapezoidal(X, a, b, c, d)
    print("Trapezoidal: Matriz de graus de pertinência:")
    for row in Mi_trapezoidal:
        print([f"{value:.2f}" for value in row])
    plot_fuzzification(X, Mi_trapezoidal, "Trapezoidal")

    # Testando a função gaussiana
    c, sigma = 5, 1  # Parâmetros da função gaussiana
    Mi_gaussian = fuzzify_gaussian(X, c, sigma)
    print("Gaussiana: Matriz de graus de pertinência:")
    for row in Mi_gaussian:
        print([f"{value:.2f}" for value in row])
    plot_fuzzification(X, Mi_gaussian, "Gaussiana")

    # Testando a função sigmoidal
    alpha, c = 0.1, 5  # Parâmetros da função sigmoidal
    Mi_sigmoidal = fuzzify_sigmoidal(X, alpha, c)
    print("Sigmoidal: Matriz de graus de pertinência:")
    for row in Mi_sigmoidal:
        print([f"{value:.2f}" for value in row])
    plot_fuzzification(X, Mi_sigmoidal, "Sigmoidal")

    # Testando a função bell
    a, b, c = 15, 2, 5  # Parâmetros da função bell
    Mi_bell = fuzzify_bell(X, a, b, c)
    print("Sino: Matriz de graus de pertinência:")
    for row in Mi_bell:
        print([f"{value:.2f}" for value in row])
    plot_fuzzification(X, Mi_bell, "Sino")

    # Testando a função S-Shaped
    a, b = 0, 10  # Parâmetros da função S-shaped
    Mi_s_shaped = fuzzify_s_shaped(X, a, b)
    print("S-Shaped: Matriz de graus de pertinência:")
    for row in Mi_s_shaped:
        print([f"{value:.2f}" for value in row])
    plot_fuzzification(X, Mi_s_shaped, "Tipo-S")

    # Testando a função Z-Shaped
    a, b = 0, 10  # Parâmetros da função Z-shaped
    Mi_z_shaped = fuzzify_z_shaped(X, a, b)
    print("Z-Shaped: Matriz de graus de pertinência:")
    for row in Mi_z_shaped:
        print([f"{value:.2f}" for value in row])
    plot_fuzzification(X, Mi_z_shaped, "Tipo-Z")

    # Testando a função Cauchy
    c, gamma = 5, 2  # Parâmetros da função Cauchy
    Mi_cauchy = fuzzify_cauchy(X, c, gamma)
    print("Cauchy: Matriz de graus de pertinência:")
    for row in Mi_cauchy:
        print([f"{value:.2f}" for value in row])
    plot_fuzzification(X, Mi_cauchy, "Cauchy")

    # Testando a função Gaussiana Dupla
    c1, sigma1, c2, sigma2 = 4, 1, 8, 1  # Parâmetros da função gaussiana dupla
    Mi_double_gaussian = fuzzify_double_gaussian(X, c1, sigma1, c2, sigma2)
    print("Gaussiana Dupla: Matriz de graus de pertinência:")
    for row in Mi_double_gaussian:
        print([f"{value:.2f}" for value in row])
    plot_fuzzification(X, Mi_double_gaussian, "Gaussiana Dupla")

    # Testando a função Linear por Partes
    a, b = 0, 10  # Parâmetros da função linear por partes
    Mi_linear_piecewise = fuzzify_linear_piecewise(X, a, b)
    print("Linear por Partes: Matriz de graus de pertinência:")
    for row in Mi_linear_piecewise:
        print([f"{value:.2f}" for value in row])
    plot_fuzzification(X, Mi_linear_piecewise, "Linear por Partes")

    # Testando a função Polinomial
    c, n = 5, 2  # Parâmetros da função polinomial
    Mi_polynomial = fuzzify_polynomial(X, c, n)
    print("Polinomial: Matriz de graus de pertinência:")
    for row in Mi_polynomial:
        print([f"{value:.2f}" for value in row])
    plot_fuzzification(X, Mi_polynomial, "Polinomial")