# fuzzy.py

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

