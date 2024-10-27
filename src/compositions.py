def fuzzy_composition_max_min(matrix_a, matrix_b):
    """
    Calcula a composição fuzzy Max-Min entre duas matrizes fuzzy, sem usar estruturas prontas.
    
    matrix_a: Primeira matriz fuzzy (lista de listas, conjunto A).
    matrix_b: Segunda matriz fuzzy (lista de listas, conjunto B).
    
    Retorna: A matriz de composição Max-Min (lista de listas).
    """
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])
    
    if cols_a != rows_b:
        raise ValueError("As dimensões das matrizes são incompatíveis para a composição Max-Min.")
    
    result = []
    
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            # Manualmente calcular o mínimo e depois o máximo (Max-Min)
            min_values = []
            for k in range(cols_a):
                min_values.append(min(matrix_a[i][k], matrix_b[k][j]))
            row.append(max(min_values))
        result.append(row)
    
    return result


def fuzzy_composition_min_max(matrix_a, matrix_b):
    """
    Calcula a composição fuzzy Min-Max entre duas matrizes fuzzy, sem usar estruturas prontas.
    
    matrix_a: Primeira matriz fuzzy (lista de listas, conjunto A).
    matrix_b: Segunda matriz fuzzy (lista de listas, conjunto B).
    
    Retorna: A matriz de composição Min-Max (lista de listas).
    """
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])
    
    if cols_a != rows_b:
        raise ValueError("As dimensões das matrizes são incompatíveis para a composição Min-Max.")
    
    result = []
    
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            # Manualmente calcular o máximo e depois o mínimo (Min-Max)
            max_values = []
            for k in range(cols_a):
                max_values.append(max(matrix_a[i][k], matrix_b[k][j]))
            row.append(min(max_values))
        result.append(row)
    
    return result


def fuzzy_composition_max_prod(matrix_a, matrix_b):
    """
    Calcula a composição fuzzy Max-Prod entre duas matrizes fuzzy, sem usar estruturas prontas.
    
    matrix_a: Primeira matriz fuzzy (lista de listas, conjunto A).
    matrix_b: Segunda matriz fuzzy (lista de listas, conjunto B).
    
    Retorna: A matriz de composição Max-Prod (lista de listas).
    """
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])
    
    if cols_a != rows_b:
        raise ValueError("As dimensões das matrizes são incompatíveis para a composição Max-Prod.")
    
    result = []
    
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            # Manualmente calcular o produto e depois o máximo (Max-Prod)
            prod_values = []
            for k in range(cols_a):
                prod_values.append(matrix_a[i][k] * matrix_b[k][j])
            row.append(max(prod_values))
        result.append(row)
    
    return result