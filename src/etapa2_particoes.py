import numpy as np
from fuzzy import (fuzzify_triangular, fuzzify_trapezoidal, fuzzify_gaussian, fuzzify_sigmoidal,
                   triangular_mf, trapezoidal_mf, gaussian_mf, sigmoidal_mf)
from utils import plot_fuzzification

def executar_etapa2():
    # Definir o domínio (universo de discurso)
    dominio = np.linspace(0, 100, 100)

    # Definir duas amostras de entrada
    amostras = np.array([25, 75])

    # 1. Funções Triangulares Uniformemente Espaçadas
    print("Fuzzificação - Funções Triangulares:")
    params_triangular = [(0, 20, 40), (20, 40, 60), (40, 60, 80), (60, 80, 100)]
    for i, (a, b, c) in enumerate(params_triangular):
        Mi_triangular = fuzzify_triangular(dominio.reshape(1, -1), a, b, c)
        print(f"Triangular {i+1}: Parâmetros: a={a}, b={b}, c={c}")
        plot_fuzzification(dominio.reshape(1, -1), Mi_triangular, f"Triangular {i+1}")
        for amostra in amostras:
            grau_pertinencia = triangular_mf(amostra, a, b, c)
            print(f"Amostra {amostra} - Grau de Pertinência: {grau_pertinencia}")

    # 2. Funções Trapezoidais Uniformemente Espaçadas
    print("Fuzzificação - Funções Trapezoidais:")
    params_trapezoidal = [(0, 15, 25, 40), (20, 35, 45, 60), (40, 55, 65, 80), (60, 75, 85, 100)]
    for i, (a, b, c, d) in enumerate(params_trapezoidal):
        Mi_trapezoidal = fuzzify_trapezoidal(dominio.reshape(1, -1), a, b, c, d)
        print(f"Trapezoidal {i+1}: Parâmetros: a={a}, b={b}, c={c}, d={d}")
        plot_fuzzification(dominio.reshape(1, -1), Mi_trapezoidal, f"Trapezoidal {i+1}")
        for amostra in amostras:
            grau_pertinencia = trapezoidal_mf(amostra, a, b, c, d)
            print(f"Amostra {amostra} - Grau de Pertinência: {grau_pertinencia}")

    # 3. Funções Gaussianas Uniformemente Espaçadas
    print("Fuzzificação - Funções Gaussianas:")
    params_gaussian = [(20, 10), (40, 10), (60, 10), (80, 10)]
    for i, (c, sigma) in enumerate(params_gaussian):
        Mi_gaussian = fuzzify_gaussian(dominio.reshape(1, -1), c, sigma)
        print(f"Gaussiana {i+1}: Parâmetros: c={c}, sigma={sigma}")
        plot_fuzzification(dominio.reshape(1, -1), Mi_gaussian, f"Gaussiana {i+1}")
        for amostra in amostras:
            grau_pertinencia = gaussian_mf(amostra, c, sigma)
            print(f"Amostra {amostra} - Grau de Pertinência: {grau_pertinencia}")

    # 4. Funções Sigmoidais Uniformemente Espaçadas
    print("Fuzzificação - Funções Sigmoidais:")
    params_sigmoidal = [(0.1, 20), (0.1, 40), (0.1, 60), (0.1, 80)]
    for i, (alpha, c) in enumerate(params_sigmoidal):
        Mi_sigmoidal = fuzzify_sigmoidal(dominio.reshape(1, -1), alpha, c)
        print(f"Sigmoidal {i+1}: Parâmetros: alpha={alpha}, c={c}")
        plot_fuzzification(dominio.reshape(1, -1), Mi_sigmoidal, f"Sigmoidal {i+1}")
        for amostra in amostras:
            grau_pertinencia = sigmoidal_mf(amostra, alpha, c)
            print(f"Amostra {amostra} - Grau de Pertinência: {grau_pertinencia}")
