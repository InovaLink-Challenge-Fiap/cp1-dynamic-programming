import pandas as pd                   
from collections import deque          
import matplotlib.pyplot as plt        

df = pd.read_csv("Check_point_1_dados_logistica_RA_final impar.csv")

print("=== DADOS CARREGADOS DO CSV ===")
print(df)
print()

lista_entregas = []

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
    lista_entregas.append(tupla) 

print("=== LISTA DE ENTREGAS (tuplas) ===")
for entrega in lista_entregas:
    print(entrega)
print()

dicionario_transportadoras = {}

for entrega in lista_entregas:
    transportadora = entrega[9]  
    if transportadora not in dicionario_transportadoras:
        dicionario_transportadoras[transportadora] = []
    dicionario_transportadoras[transportadora].append(entrega[0]) 

print("=== ENTREGAS POR TRANSPORTADORA (dicionário) ===")
for transportadora, ids in dicionario_transportadoras.items():
    print(f"Transportadora {transportadora}: entregas {ids}")
print()

fila_entregas = deque()

for entrega in lista_entregas:
    fila_entregas.append(entrega)

print("=== FILA DE ENTREGAS (deque) ===")
print(f"Total de entregas na fila: {len(fila_entregas)}")
print(f"Primeira entrega da fila: {fila_entregas[0][0]} - {fila_entregas[0][1]} → {fila_entregas[0][2]}")
print(f"Última entrega da fila:   {fila_entregas[-1][0]} - {fila_entregas[-1][1]} → {fila_entregas[-1][2]}")
print()

peso_situacao = {'critica': 0, 'atencao': 1, 'livre': 2}
peso_prioridade = {'vip': 0, 'normal': 1}

entregas_ordenadas = sorted(lista_entregas, key=lambda e: (peso_situacao[e[8]], peso_prioridade[e[7]], e[6]))

print("=== ORDEM DE SAÍDA DAS ENTREGAS (por prioridade) ===")
for i, entrega in enumerate(entregas_ordenadas, 1):
    print(f"{i}º - Entrega {entrega[0]} | {entrega[1]}→{entrega[2]} | Rota: {entrega[8]} | Cliente: {entrega[7]} | Prazo: {entrega[6]} dias")
print()

