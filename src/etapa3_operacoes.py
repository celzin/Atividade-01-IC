import numpy as np
from fuzzy import fuzzify_trapezoidal
from operations import (fuzzy_complement, fuzzy_union, fuzzy_intersection,
                        fuzzy_tnorm_product, fuzzy_snorm_probabilistic)
from utils import plot_fuzzification_operations

def executar_etapa3():
    # Definir o domínio (universo de discurso)
    dominio = np.linspace(0, 100, 100).reshape(1, -1) 

    # Funções Trapezoidais para testes
    params_trapezoidal = [(0, 15, 35, 50), (30, 45, 65, 80)]
    Mi_trapezoidal1 = fuzzify_trapezoidal(dominio, *params_trapezoidal[0])
    Mi_trapezoidal2 = fuzzify_trapezoidal(dominio, *params_trapezoidal[1])

    # Pontos de interesse para análise comparativa
    pontos_interesse = [0, 25, 50, 75, 100]

    # Função auxiliar para exibir valores de pertinência em pontos de interesse
    def exibir_valores_operacao(nome_operacao, valores):
        print(f"\nValores de Pertinência - {nome_operacao}:")
        for ponto in pontos_interesse:
            idx = np.abs(dominio - ponto).argmin()  # Encontrar índice mais próximo do ponto
            print(f"Domínio {ponto}: {valores[idx]:.2f}")

    # 1. Complemento
    Mi_complement = fuzzy_complement(Mi_trapezoidal1[0])
    exibir_valores_operacao("Complemento", Mi_complement)
    plot_fuzzification_operations(dominio[0], [Mi_trapezoidal1[0], Mi_complement], "Complemento")

    # 2. União (Máximo)
    Mi_union = fuzzy_union(Mi_trapezoidal1[0], Mi_trapezoidal2[0])
    exibir_valores_operacao("União", Mi_union)
    plot_fuzzification_operations(dominio[0], [Mi_trapezoidal1[0], Mi_trapezoidal2[0], Mi_union], "União")

    # 3. Interseção (Mínimo)
    Mi_intersection = fuzzy_intersection(Mi_trapezoidal1[0], Mi_trapezoidal2[0])
    exibir_valores_operacao("Interseção", Mi_intersection)
    plot_fuzzification_operations(dominio[0], [Mi_trapezoidal1[0], Mi_trapezoidal2[0], Mi_intersection], "Interseção")

    # 4. Normas Duais (Produto Algébrico e Soma Probabilística)
    Mi_tnorm = fuzzy_tnorm_product(Mi_trapezoidal1[0], Mi_trapezoidal2[0])
    exibir_valores_operacao("T-Norm Produto", Mi_tnorm)
    plot_fuzzification_operations(dominio[0], [Mi_trapezoidal1[0], Mi_trapezoidal2[0], Mi_tnorm], "Produto")

    Mi_snorm = fuzzy_snorm_probabilistic(Mi_trapezoidal1[0], Mi_trapezoidal2[0])
    exibir_valores_operacao("S-Norm Probabilística", Mi_snorm)
    plot_fuzzification_operations(dominio[0], [Mi_trapezoidal1[0], Mi_trapezoidal2[0], Mi_snorm], "Soma Probabilística")