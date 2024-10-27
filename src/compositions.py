def fuzzy_composition_max_min(matrix_a, matrix_b):
    """
    Calcula a composição fuzzy Max-Min entre duas matrizes fuzzy.
    
    matrix_a: Primeira matriz fuzzy (conjunto fuzzy A).
    matrix_b: Segunda matriz fuzzy (conjunto fuzzy B).
    
    Retorna: A matriz de composição Max-Min.
    """
    rows_a, cols_a = len(matrix_a), len(matrix_a[0])
    rows_b, cols_b = len(matrix_b), len(matrix_b[0])
    
    if cols_a != rows_b:
        raise ValueError("As dimensões das matrizes são incompatíveis para a composição Max-Min.")
    
    result = []
    
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            # Max-Min: Para cada par (i, j), calcular o máximo do mínimo
            min_values = [min(matrix_a[i][k], matrix_b[k][j]) for k in range(cols_a)]
            row.append(max(min_values))
        result.append(row)
    
    return result


def fuzzy_composition_min_max(matrix_a, matrix_b):
    """
    Calcula a composição fuzzy Min-Max entre duas matrizes fuzzy.
    
    matrix_a: Primeira matriz fuzzy (conjunto fuzzy A).
    matrix_b: Segunda matriz fuzzy (conjunto fuzzy B).
    
    Retorna: A matriz de composição Min-Max.
    """
    rows_a, cols_a = len(matrix_a), len(matrix_a[0])
    rows_b, cols_b = len(matrix_b), len(matrix_b[0])
    
    if cols_a != rows_b:
        raise ValueError("As dimensões das matrizes são incompatíveis para a composição Min-Max.")
    
    result = []
    
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            # Min-Max: Para cada par (i, j), calcular o mínimo do máximo
            max_values = [max(matrix_a[i][k], matrix_b[k][j]) for k in range(cols_a)]
            row.append(min(max_values))
        result.append(row)
    
    return result


def fuzzy_composition_max_prod(matrix_a, matrix_b):
    """
    Calcula a composição fuzzy Max-Prod entre duas matrizes fuzzy.
    
    matrix_a: Primeira matriz fuzzy (conjunto fuzzy A).
    matrix_b: Segunda matriz fuzzy (conjunto fuzzy B).
    
    Retorna: A matriz de composição Max-Prod.
    """
    rows_a, cols_a = len(matrix_a), len(matrix_a[0])
    rows_b, cols_b = len(matrix_b), len(matrix_b[0])
    
    if cols_a != rows_b:
        raise ValueError("As dimensões das matrizes são incompatíveis para a composição Max-Prod.")
    
    result = []
    
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            # Max-Prod: Para cada par (i, j), calcular o máximo do produto
            prod_values = [matrix_a[i][k] * matrix_b[k][j] for k in range(cols_a)]
            row.append(max(prod_values))
        result.append(row)
    
    return result
