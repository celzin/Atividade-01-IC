import numpy as np
from fuzzy import (fuzzify_triangular, fuzzify_trapezoidal, fuzzify_gaussian, fuzzify_sigmoidal, 
                   fuzzify_bell, fuzzify_s_shaped, fuzzify_z_shaped, fuzzify_cauchy, 
                   fuzzify_double_gaussian, fuzzify_linear_piecewise, fuzzify_polynomial)
from utils import plot_fuzzification

if __name__ == "__main__":
    # Definir o domínio (universo de discurso)
    dominio = np.linspace(0, 100, 100)  # 100 pontos no intervalo de 0 a 100

    # Testando a função triangular
    a, b, c = 20, 50, 80  # Parâmetros da função triangular
    Mi_triangular = fuzzify_triangular(dominio.reshape(1, -1), a, b, c)
    print("Triangular: Matriz de graus de pertinência:")
    for row in Mi_triangular:
        print([f"{value:.2f}" for value in row])
    plot_fuzzification(dominio.reshape(1, -1), Mi_triangular, "Triangular")

    # Testando a função trapezoidal
    a, b, c, d = 10, 30, 70, 90  # Parâmetros da função trapezoidal
    Mi_trapezoidal = fuzzify_trapezoidal(dominio.reshape(1, -1), a, b, c, d)
    print("Trapezoidal: Matriz de graus de pertinência:")
    for row in Mi_trapezoidal:
        print([f"{value:.2f}" for value in row])
    plot_fuzzification(dominio.reshape(1, -1), Mi_trapezoidal, "Trapezoidal")

    # Testando a função gaussiana
    c, sigma = 50, 15  # Parâmetros da função gaussiana
    Mi_gaussian = fuzzify_gaussian(dominio.reshape(1, -1), c, sigma)
    print("Gaussiana: Matriz de graus de pertinência:")
    for row in Mi_gaussian:
        print([f"{value:.2f}" for value in row])
    plot_fuzzification(dominio.reshape(1, -1), Mi_gaussian, "Gaussiana")

    # Testando a função sigmoidal
    alpha, c = 0.1, 50  # Parâmetros da função sigmoidal
    Mi_sigmoidal = fuzzify_sigmoidal(dominio.reshape(1, -1), alpha, c)
    print("Sigmoidal: Matriz de graus de pertinência:")
    for row in Mi_sigmoidal:
        print([f"{value:.2f}" for value in row])
    plot_fuzzification(dominio.reshape(1, -1), Mi_sigmoidal, "Sigmoidal")

    # Testando a função bell
    a, b, c = 15, 2, 50  # Parâmetros da função bell
    Mi_bell = fuzzify_bell(dominio.reshape(1, -1), a, b, c)
    print("Sino: Matriz de graus de pertinência:")
    for row in Mi_bell:
        print([f"{value:.2f}" for value in row])
    plot_fuzzification(dominio.reshape(1, -1), Mi_bell, "Sino")

    # Testando a função Tipo-S
    a, b = 20, 80  # Parâmetros da função Tipo-S
    Mi_s_shaped = fuzzify_s_shaped(dominio.reshape(1, -1), a, b)
    print("Tipo-S: Matriz de graus de pertinência:")
    for row in Mi_s_shaped:
        print([f"{value:.2f}" for value in row])
    plot_fuzzification(dominio.reshape(1, -1), Mi_s_shaped, "Tipo-S")

    # Testando a função Tipo-Z
    a, b = 20, 80  # Parâmetros da função Tipo-Z
    Mi_z_shaped = fuzzify_z_shaped(dominio.reshape(1, -1), a, b)
    print("Tipo-Z: Matriz de graus de pertinência:")
    for row in Mi_z_shaped:
        print([f"{value:.2f}" for value in row])
    plot_fuzzification(dominio.reshape(1, -1), Mi_z_shaped, "Tipo-Z")

    # Testando a função Cauchy
    c, gamma = 50, 20  # Parâmetros da função Cauchy
    Mi_cauchy = fuzzify_cauchy(dominio.reshape(1, -1), c, gamma)
    print("Cauchy: Matriz de graus de pertinência:")
    for row in Mi_cauchy:
        print([f"{value:.2f}" for value in row])
    plot_fuzzification(dominio.reshape(1, -1), Mi_cauchy, "Cauchy")

    # Testando a função Gaussiana Dupla
    c1, sigma1, c2, sigma2 = 40, 10, 60, 10  # Parâmetros da função gaussiana dupla
    Mi_double_gaussian = fuzzify_double_gaussian(dominio.reshape(1, -1), c1, sigma1, c2, sigma2)
    print("Gaussiana Dupla: Matriz de graus de pertinência:")
    for row in Mi_double_gaussian:
        print([f"{value:.2f}" for value in row])
    plot_fuzzification(dominio.reshape(1, -1), Mi_double_gaussian, "Gaussiana Dupla")

    # Testando a função Linear por Partes
    a, b = 20, 80  # Parâmetros da função linear por partes
    Mi_linear_piecewise = fuzzify_linear_piecewise(dominio.reshape(1, -1), a, b)
    print("Linear por Partes: Matriz de graus de pertinência:")
    for row in Mi_linear_piecewise:
        print([f"{value:.2f}" for value in row])
    plot_fuzzification(dominio.reshape(1, -1), Mi_linear_piecewise, "Linear por Partes")

    # Testando a função Polinomial
    c, n = 50, 2  # Parâmetros da função polinomial
    Mi_polynomial = fuzzify_polynomial(dominio.reshape(1, -1), c, n)
    print("Polinomial: Matriz de graus de pertinência:")
    for row in Mi_polynomial:
        print([f"{value:.2f}" for value in row])
    plot_fuzzification(dominio.reshape(1, -1), Mi_polynomial, "Polinomial")
