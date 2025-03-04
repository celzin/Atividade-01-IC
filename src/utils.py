import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def plot_fuzzification(X, Mi, function_name):
    """
    Função para plotar os resultados da fuzzificação.
    X: Matriz de entrada original.
    Mi: Matriz de graus de pertinência (fuzzificada).
    function_name: Nome da função de pertinência sendo plotada.
    """
    for i in range(len(X)):
        plt.plot(X[i], Mi[i], label=f'Conjunto {i+1}')
    
    plt.title(f'Fuzzificação dos Conjuntos de Dados - {function_name}')
    plt.xlabel('Valores de Entrada')
    plt.ylabel('Grau de Pertinência')
    plt.legend()
    plt.show()


def plot_fuzzification_overlay(X, Mis, function_name):
    """
    Função para plotar os resultados da fuzzificação com sobreposição de funções.
    X: Matriz de entrada original.
    Mis: Lista de matrizes de graus de pertinência (fuzzificadas).
    function_name: Nome da função de pertinência sendo plotada.
    """
    for i, Mi in enumerate(Mis):
        plt.plot(X[0], Mi[0], label=f'Conjunto {i+1}')
    
    plt.title(f'Fuzzificação dos Conjuntos - Sobreposição ({function_name})')
    plt.xlabel('Valores de Entrada')
    plt.ylabel('Grau de Pertinência')
    plt.legend()
    plt.show()

def plot_fuzzification_operations(X, Mis, operation_name):
    # Ajuste da legenda dependendo da operação
    if operation_name == "Complemento":
        labels = ["Conjunto 1", "Complemento"]
    elif operation_name in ["União", "Interseção", "Produto", "Soma Probabilística"]:
        labels = [f"Conjunto {i+1}" for i in range(len(Mis)-1)] + [f"{operation_name}"]
    else:
        labels = [f"Conjunto {i+1}" for i in range(len(Mis))]

    # Plotar cada conjunto com seu rótulo
    for i, Mi in enumerate(Mis):
        plt.plot(X, Mi, label=labels[i])

    plt.title(f"Operações Fuzzy - {operation_name}")
    plt.xlabel("Valores de Entrada")
    plt.ylabel("Grau de Pertinência")
    plt.legend()
    plt.show()

def plot_fuzzy_membership(dominio, membership_values, conjunto_nome, x_label):
    """
    Plota um gráfico de pertinência fuzzy semelhante ao da imagem fornecida.
    
    dominio: O domínio dos valores (ex: altura, idade).
    membership_values: Valores de pertinência correspondentes ao domínio.
    conjunto_nome: Nome do conjunto fuzzy (ex: 'ALTO', 'MEIA-IDADE').
    x_label: Rótulo para o eixo X (ex: 'Altura', 'Idade').
    """
    plt.plot(dominio, membership_values, linewidth=2, color='gray')
    plt.fill_between(dominio, 0, membership_values, color='gray', alpha=0.5)
    
    plt.title(f'Conjunto {conjunto_nome}')
    plt.xlabel(x_label)
    plt.ylabel('Grau de Pertinência')
    plt.ylim(0, 1)
    plt.grid(True)
    plt.show()

def plot_comparison_membership(dominio_altura, altura_values, dominio_idade, idade_values):
    """
    Gera dois gráficos lado a lado: um para 'ALTO' e outro para 'MEIA-IDADE', conforme exemplo da imagem.
    
    dominio_altura: Valores de altura.
    altura_values: Graus de pertinência para altura.
    dominio_idade: Valores de idade.
    idade_values: Graus de pertinência para idade.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Gráfico para o conjunto ALTO
    ax1.plot(dominio_altura, altura_values, linewidth=2, color='gray')
    ax1.fill_between(dominio_altura, 0, altura_values, color='gray', alpha=0.5)
    ax1.set_title('Conjunto ALTO')
    ax1.set_xlabel('Altura')
    ax1.set_ylabel('Grau de Pertinência')
    ax1.set_ylim(0, 1)
    ax1.grid(True)

    # Gráfico para o conjunto MEIA-IDADE
    ax2.plot(dominio_idade, idade_values, linewidth=2, color='gray')
    ax2.fill_between(dominio_idade, 0, idade_values, color='gray', alpha=0.5)
    ax2.set_title('Conjunto MEIA-IDADE')
    ax2.set_xlabel('Idade')
    ax2.set_ylabel('Grau de Pertinência')
    ax2.set_ylim(0, 1)
    ax2.grid(True)

    plt.tight_layout()
    plt.show()

def plot_heatmap(matrix, title):
    """
    Plota um heatmap da matriz de relação fuzzy.
    
    matrix: Matriz de relação fuzzy.
    title: Título do gráfico (indica o tipo de norma usada).
    """
    plt.figure(figsize=(8, 6))
    sns.heatmap(matrix, annot=True, cmap="YlGnBu", cbar=True)
    plt.title(f"Heatmap da Relação Fuzzy - {title}")
    plt.xlabel("Conjunto 1 (Altura)")
    plt.ylabel("Conjunto 2 (Idade)")
    plt.show()

def plot_fuzzy_compositions(matrix_max_min, matrix_min_max, matrix_max_prod):
    """
    Plota os resultados das três composições fuzzy: Max-Min, Min-Max e Max-Prod.
    
    matrix_max_min: Matriz resultante da composição Max-Min.
    matrix_min_max: Matriz resultante da composição Min-Max.
    matrix_max_prod: Matriz resultante da composição Max-Prod.
    """
    # Definir os títulos e dados para comparação
    titles = ['Composição Max-Min', 'Composição Min-Max', 'Composição Max-Prod']
    matrices = [matrix_max_min, matrix_min_max, matrix_max_prod]
    
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    for ax, title, matrix in zip(axs, titles, matrices):
        ax.matshow(matrix, cmap='coolwarm', aspect='auto')
        for (i, j), val in np.ndenumerate(matrix):
            ax.text(j, i, f'{val:.2f}', ha='center', va='center', color='black')
        ax.set_title(title)
        ax.set_xlabel("Conjunto B (Idade)")
        ax.set_ylabel("Conjunto A (Altura)")
    
    plt.tight_layout()
    plt.show()