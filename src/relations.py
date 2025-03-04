def fuzzy_relation_binaria(op_norma, set_a, set_b):
    """
    Calcula uma relação binária fuzzy entre dois conjuntos fuzzy usando uma t-norma ou s-norma.
    
    op_norma: Função de t-norma ou s-norma.
    set_a: Lista de graus de pertinência do conjunto A.
    set_b: Lista de graus de pertinência do conjunto B.
    
    Retorna: Matriz de relação fuzzy binária.
    """
    if len(set_a) != len(set_b):
        raise ValueError("Os dois conjuntos devem ter o mesmo tamanho.")
    
    # Matriz de relação fuzzy binária
    relation_matrix = []
    
    for i in range(len(set_a)):
        row = []
        for j in range(len(set_b)):
            # Aplicar a norma para calcular o grau de relação entre os elementos
            relation_value = op_norma(set_a[i], set_b[j])
            row.append(relation_value)
        relation_matrix.append(row)
    
    return relation_matrix

def tnorm_diferenca_limitada(x, y):
    """
    T-norma de Diferença Limitada para relação fuzzy.
    x: Grau de pertinência do primeiro conjunto.
    y: Grau de pertinência do segundo conjunto.
    
    Retorna: Grau de pertinência após aplicar a t-norma de diferença limitada.
    """
    return max(0, x + y - 1)

def tnorm_min(x, y):
    """
    T-norma de Interseção Mínima para relação fuzzy.
    x: Grau de pertinência do primeiro conjunto.
    y: Grau de pertinência do segundo conjunto.
    
    Retorna: O mínimo entre x e y.
    """
    return min(x, y)

# S-Norma de Soma Probabilística
def s_norma_soma_probabilistica(x, y):
    """
    S-Norma de Soma Probabilística para relação fuzzy.
    x: Grau de pertinência do primeiro conjunto.
    y: Grau de pertinência do segundo conjunto.
    
    Retorna: Grau de pertinência após aplicar a s-norma de soma probabilística.
    """
    return x + y - (x * y)

# S-Norma de Soma Limitada
def s_norma_soma_limitada(x, y):
    """
    S-Norma de Soma Limitada para relação fuzzy.
    x: Grau de pertinência do primeiro conjunto.
    y: Grau de pertinência do segundo conjunto.
    
    Retorna: Grau de pertinência após aplicar a s-norma de soma limitada.
    """
    return min(1, x + y)
