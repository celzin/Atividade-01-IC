import numpy as np

# 1. Triangular
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

def fuzzify_triangular(X, a, b, c):
    M, N = X.shape
    Mi = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            Mi[i][j] = triangular_mf(X[i][j], a, b, c)
    return Mi

# 2. Trapezoidal
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

def fuzzify_trapezoidal(X, a, b, c, d):
    M, N = X.shape
    Mi = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            Mi[i][j] = trapezoidal_mf(X[i][j], a, b, c, d)
    return Mi

# 3. Gaussiana
def gaussian_mf(x, c, sigma):
    """
    Função de pertinência Gaussiana.
    x: valor de entrada
    c: valor central
    sigma: desvio padrão
    """
    return np.exp(-0.5 * ((x - c) / sigma) ** 2)

def fuzzify_gaussian(X, c, sigma):
    M, N = X.shape
    Mi = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            Mi[i][j] = gaussian_mf(X[i][j], c, sigma)
    return Mi

# 4. Sigmoidal
def sigmoidal_mf(x, alpha, c):
    """
    Função de pertinência Sigmoidal.
    x: valor de entrada
    alpha: inclinação da curva
    c: ponto central
    """
    return 1 / (1 + np.exp(-alpha * (x - c)))

def fuzzify_sigmoidal(X, alpha, c):
    M, N = X.shape
    Mi = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            Mi[i][j] = sigmoidal_mf(X[i][j], alpha, c)
    return Mi

# 5. Sino
def bell_mf(x, a, b, c):
    """
    Função de pertinência Sino.
    a: largura da curva
    b: inclinação
    c: valor central
    """
    return 1 / (1 + abs((x - c) / a) ** (2 * b))

def fuzzify_bell(X, a, b, c):
    M, N = X.shape
    Mi = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            Mi[i][j] = bell_mf(X[i][j], a, b, c)
    return Mi

# 6. Função-S
def s_shaped_mf(x, a, b):
    """
    Função de pertinência em 'S' (S-shaped).
    x: valor de entrada
    a: limite inferior (Mi = 0)
    b: limite superior (Mi = 1)
    """
    if x <= a:
        return 0.0
    elif a < x <= (a + b) / 2:
        return 2 * ((x - a) / (b - a)) ** 2
    elif (a + b) / 2 < x <= b:
        return 1 - 2 * ((b - x) / (b - a)) ** 2
    else:
        return 1.0

def fuzzify_s_shaped(X, a, b):
    M, N = X.shape
    Mi = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            Mi[i][j] = s_shaped_mf(X[i][j], a, b)
    return Mi

# 7. Função-Z
def z_shaped_mf(x, a, b):
    """
    Função de pertinência em 'Z' (Z-shaped).
    x: valor de entrada
    a: limite inferior (Mi = 1)
    b: limite superior (Mi = 0)
    """
    if x <= a:
        return 1.0
    elif a < x <= (a + b) / 2:
        return 1 - 2 * ((x - a) / (b - a)) ** 2
    elif (a + b) / 2 < x <= b:
        return 2 * ((b - x) / (b - a)) ** 2
    else:
        return 0.0

def fuzzify_z_shaped(X, a, b):
    M, N = X.shape
    Mi = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            Mi[i][j] = z_shaped_mf(X[i][j], a, b)
    return Mi

# 8. Cauchy
def cauchy_mf(x, c, gamma):
    """
    Função de pertinência Cauchy.
    x: valor de entrada
    c: valor central
    gamma: largura da curva
    """
    return 1 / (1 + ((x - c) / gamma) ** 2)

def fuzzify_cauchy(X, c, gamma):
    M, N = X.shape
    Mi = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            Mi[i][j] = cauchy_mf(X[i][j], c, gamma)
    return Mi

# 9. Gaussiana Dupla
def double_gaussian_mf(x, c1, sigma1, c2, sigma2):
    """
    Função de pertinência Gaussiana Dupla.
    x: valor de entrada
    c1, c2: valores centrais das gaussianas
    sigma1, sigma2: desvios padrão das gaussianas
    """
    return np.exp(-0.5 * ((x - c1) / sigma1) ** 2) + np.exp(-0.5 * ((x - c2) / sigma2) ** 2)

def fuzzify_double_gaussian(X, c1, sigma1, c2, sigma2):
    M, N = X.shape
    Mi = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            Mi[i][j] = double_gaussian_mf(X[i][j], c1, sigma1, c2, sigma2)
    return Mi

# 10. User definied 1 - Linear por Partes
def linear_piecewise_mf(x, a, b):
    """
    Função Linear por Partes (Linear Piecewise).
    a: limite inferior
    b: limite superior
    """
    if x < a:
        return 0.0
    elif a <= x <= b:
        return (x - a) / (b - a)
    else:
        return 1.0

def fuzzify_linear_piecewise(X, a, b):
    M, N = X.shape
    Mi = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            Mi[i][j] = linear_piecewise_mf(X[i][j], a, b)
    return Mi

# 11. User definied 2 - Polinomial
def polynomial_mf(x, c, n):
    """
    Função Polinomial.
    c: valor central
    n: expoente do polinômio
    """
    return 1 - (x - c) ** n

def fuzzify_polynomial(X, c, n):
    M, N = X.shape
    Mi = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            Mi[i][j] = polynomial_mf(X[i][j], c, n)
    return Mi