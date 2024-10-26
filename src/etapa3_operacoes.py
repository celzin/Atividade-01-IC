import numpy as np
from fuzzy import fuzzify_triangular
from operations import (fuzzy_complement, fuzzy_union, fuzzy_intersection,
                              fuzzy_tnorm_product, fuzzy_snorm_probabilistic)
from utils import plot_fuzzification_operations

def executar_etapa3():
    # Definir o domínio (universo de discurso)
    dominio = np.linspace(0, 100, 100).reshape(1, -1)  # Utilizando o formato de matriz compatível com o restante do programa

    # Funções Triangulares para testes
    params_triangular = [(0, 20, 40), (20, 40, 60)]
    Mi_triangular1 = fuzzify_triangular(dominio, *params_triangular[0])
    Mi_triangular2 = fuzzify_triangular(dominio, *params_triangular[1])

    # 1. Complemento
    Mi_complement = fuzzy_complement(Mi_triangular1[0])
    plot_fuzzification_operations(dominio[0], [Mi_triangular1[0], Mi_complement], "Complemento")

    # 2. União (Máximo)
    Mi_union = fuzzy_union(Mi_triangular1[0], Mi_triangular2[0])
    plot_fuzzification_operations(dominio[0], [Mi_triangular1[0], Mi_triangular2[0], Mi_union], "União")

    # 3. Interseção (Mínimo)
    Mi_intersection = fuzzy_intersection(Mi_triangular1[0], Mi_triangular2[0])
    plot_fuzzification_operations(dominio[0], [Mi_triangular1[0], Mi_triangular2[0], Mi_intersection], "Interseção")

    # 4. Normas Duais (Produto Algébrico e Soma Probabilística)
    Mi_tnorm = fuzzy_tnorm_product(Mi_triangular1[0], Mi_triangular2[0])
    Mi_snorm = fuzzy_snorm_probabilistic(Mi_triangular1[0], Mi_triangular2[0])
    plot_fuzzification_operations(dominio[0], [Mi_triangular1[0], Mi_triangular2[0], Mi_tnorm], "T-Norm Produto")
    plot_fuzzification_operations(dominio[0], [Mi_triangular1[0], Mi_triangular2[0], Mi_snorm], "S-Norm Probabilística")
