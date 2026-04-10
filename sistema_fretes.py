"""
Sistema de Fretes e Entregas - Checkpoint 1 (Dynamic Programming - FIAP)

Descrição:
Este sistema simula o gerenciamento de entregas logísticas, utilizando
estruturas de dados como listas, tuplas, dicionários e filas (deque).
Também implementa ordenação por prioridade, recursão e geração de gráficos.

Critérios de priorização:
1. Situação da rota (critica > atencao > livre)
2. Prazo (menor prazo primeiro)
3. Valor do frete (maior valor primeiro)

Autores:
Eduardo Delorenzo Moraes - RM561749
Kauê de Almeida Pena - 564211
Lucas Rowlands Abat - 562994
Ronaldo Aparecido Monteiro Almeida - 565017
William Queiroz - 565032
"""

import pandas as pd
from collections import deque
import matplotlib.pyplot as plt


def carregar_dados(caminho_csv):
    """
    Carrega os dados do arquivo CSV utilizando pandas.

    :param caminho_csv: Caminho do arquivo CSV
    :return: DataFrame com os dados
    """
    df = pd.read_csv(caminho_csv)
    print("=== DADOS CARREGADOS DO CSV ===")
    print(df)
    print()
    return df


def criar_lista_entregas(df):
    """
    Converte o DataFrame em uma lista de tuplas imutáveis.

    :param df: DataFrame com os dados
    :return: Lista de tuplas representando entregas
    """
    lista = []

    for _, linha in df.iterrows():
        tupla = (
            int(linha['entrega_id']),
            linha['origem'],
            linha['destino'],
            linha['tipo_carga'],
            float(linha['peso_kg']),
            float(linha['valor_frete']),
            int(linha['prazo_dias']),
            linha['prioridade_cliente'],
            linha['situacao_rota'],
            linha['transportadora']
        )
        lista.append(tupla)

    return lista


def agrupar_por_transportadora(lista_entregas):
    """
    Agrupa entregas por transportadora usando dicionário.

    :param lista_entregas: Lista de entregas
    :return: Dicionário {transportadora: [ids]}
    """
    dicionario = {}

    for entrega in lista_entregas:
        transportadora = entrega[9]
        if transportadora not in dicionario:
            dicionario[transportadora] = []
        dicionario[transportadora].append(entrega[0])

    return dicionario


def criar_fila(lista_entregas):
    """
    Cria uma fila (deque) com as entregas.

    :param lista_entregas: Lista de entregas
    :return: deque com entregas
    """
    fila = deque(lista_entregas)
    return fila


def ordenar_entregas(lista_entregas):
    """
    Ordena as entregas por prioridade:
    1. Situação da rota
    2. Prazo
    3. Valor do frete (decrescente)

    :param lista_entregas: Lista de entregas
    :return: Lista ordenada
    """
    peso_situacao = {'critica': 0, 'atencao': 1, 'livre': 2}

    return sorted(
        lista_entregas,
        key=lambda e: (peso_situacao[e[8]], e[6], -e[5])
    )

def calcular_valor_total_recursivo(entregas, index=0):
    """
    Calcula o valor total dos fretes usando recursão.

    :param entregas: Lista de entregas
    :param index: Índice atual
    :return: Soma total dos fretes
    """
    if index >= len(entregas):
        return 0

    return entregas[index][5] + calcular_valor_total_recursivo(entregas, index + 1)


def processar_fila_recursivo(fila):
    """
    Processa a fila de entregas recursivamente.

    :param fila: deque de entregas
    """
    if not fila:
        print("Fila totalmente processada!")
        return

    entrega = fila.popleft()
    print(f"Processando entrega {entrega[0]} ({entrega[1]} → {entrega[2]})")

    processar_fila_recursivo(fila)


# =========================
# 📊 GRÁFICOS
# =========================

def grafico_entregas_por_transportadora(dicionario):
    """
    Gera gráfico de barras com número de entregas por transportadora.
    """
    transportadoras = list(dicionario.keys())
    quantidades = [len(ids) for ids in dicionario.values()]

    plt.figure()
    plt.bar(transportadoras, quantidades)
    plt.title("Entregas por Transportadora")
    plt.xlabel("Transportadora")
    plt.ylabel("Quantidade")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def grafico_frete_por_transportadora(lista_entregas):
    """
    Gera gráfico de valor total de frete por transportadora.
    """
    valores = {}

    for entrega in lista_entregas:
        transportadora = entrega[9]
        valores[transportadora] = valores.get(transportadora, 0) + entrega[5]

    plt.figure()
    plt.bar(valores.keys(), valores.values())
    plt.title("Valor Total de Frete por Transportadora")
    plt.xlabel("Transportadora")
    plt.ylabel("Valor (R$)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def grafico_situacao_rota(lista_entregas):
    """
    Gera gráfico de pizza com distribuição das situações de rota.
    """
    situacoes = {}

    for entrega in lista_entregas:
        situacao = entrega[8]
        situacoes[situacao] = situacoes.get(situacao, 0) + 1

    plt.figure()
    plt.pie(situacoes.values(), labels=situacoes.keys(), autopct='%1.1f%%')
    plt.title("Distribuição das Situações de Rota")
    plt.show()


# =========================
# 🚀 EXECUÇÃO
# =========================

df = carregar_dados("Check_point_1_dados_logistica_RA_final impar.csv")

lista_entregas = criar_lista_entregas(df)

print("=== LISTA DE ENTREGAS ===")
for e in lista_entregas:
    print(e)
print()

dicionario = agrupar_por_transportadora(lista_entregas)

print("=== ENTREGAS POR TRANSPORTADORA ===")
for t, ids in dicionario.items():
    print(f"{t}: {ids}")
print()

fila = criar_fila(lista_entregas)

print("=== FILA ===")
print(f"Total: {len(fila)}")
print()

ordenadas = ordenar_entregas(lista_entregas)

print("=== PRIORIDADE DE ENTREGA ===")
for i, e in enumerate(ordenadas, 1):
    print(f"{i}º - Entrega: {e[0]} | Prazo: {e[6]} | Frete: R${e[5]}")
print()


total_frete = calcular_valor_total_recursivo(lista_entregas)
print(f"\nValor total de fretes (recursivo): R${total_frete:.2f}")

print("\n=== PROCESSAMENTO RECURSIVO DA FILA ===")
processar_fila_recursivo(fila.copy())


# 📊 Gráficos
grafico_entregas_por_transportadora(dicionario)
grafico_frete_por_transportadora(lista_entregas)
grafico_situacao_rota(lista_entregas)