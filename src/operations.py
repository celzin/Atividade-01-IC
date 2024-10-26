import numpy as np

# 1. Complemento
def fuzzy_complement(memberships):
    """
    Calcula o complemento de um conjunto fuzzy.
    memberships: Lista de graus de pertinência.
    Retorna: Lista com o complemento fuzzy.
    """
    return [1 - mi for mi in memberships]


# 2. União (máximo)
def fuzzy_union(memberships1, memberships2):
    """
    Calcula a união fuzzy (máximo) entre dois conjuntos fuzzy.
    memberships1, memberships2: Listas de graus de pertinência.
    Retorna: Lista com o resultado da união fuzzy.
    """
    return [max(mi1, mi2) for mi1, mi2 in zip(memberships1, memberships2)]


# 3. Interseção (mínimo)
def fuzzy_intersection(memberships1, memberships2):
    """
    Calcula a interseção fuzzy (mínimo) entre dois conjuntos fuzzy.
    memberships1, memberships2: Listas de graus de pertinência.
    Retorna: Lista com o resultado da interseção fuzzy.
    """
    return [min(mi1, mi2) for mi1, mi2 in zip(memberships1, memberships2)]


# 4. Normas Duais
# T-Norma: Produto Algébrico
def fuzzy_tnorm_product(memberships1, memberships2):
    """
    Calcula a t-norm de produto (interseção alternativa).
    memberships1, memberships2: Listas de graus de pertinência.
    Retorna: Lista com o resultado da t-norm de produto.
    """
    return [mi1 * mi2 for mi1, mi2 in zip(memberships1, memberships2)]

# S-Norma: Soma Probabilística
def fuzzy_snorm_probabilistic(memberships1, memberships2):
    """
    Calcula a s-norm probabilística (união alternativa).
    memberships1, memberships2: Listas de graus de pertinência.
    Retorna: Lista com o resultado da s-norm probabilística.
    """
    return [mi1 + mi2 - (mi1 * mi2) for mi1, mi2 in zip(memberships1, memberships2)]











