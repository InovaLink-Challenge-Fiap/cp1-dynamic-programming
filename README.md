# Sistema de Fretes e Entregas - CP1 Dynamic Programming

## 📋 Descrição
Sistema de simulação de fretes e entregas desenvolvido em Python para o Checkpoint 1 da disciplina de Dynamic Programming da FIAP.

## 👥 Grupo
- Eduardo Delorenzo Moraes - RM561749
- Kauê de Almeida Pena - 564211
- Lucas Rowlands Abat - 562994
- Ronaldo Aparecido Monteiro Almeida - 565017
- William Queiroz - 565032

## 🎯 Enunciado
Enunciado B (RA Ímpar) - Simular sistema de fretes e entregas, priorizando cargas por custo, prazo e criticidade.

## 🔧 Estruturas de Dados Utilizadas
- **DataFrame** - Leitura e carregamento dos dados do CSV
- **Lista** - Armazenamento de todas as entregas
- **Tupla** - Representação imutável de cada entrega
- **Dicionário** - Agrupamento das entregas por transportadora
- **Deque** - Fila de entregas aguardando processamento

## 📊 Funcionalidades implementadas
- Leitura do CSV com pandas
- Conversão dos dados em tuplas imutáveis
- Agrupamento por transportadora
- Fila de entregas com deque
- Ordenação por prioridade (situação da rota → cliente → prazo)

## 🚧 A completar
- Recursão
- Gráficos
- Relatório explicativo

## ▶️ Como executar
```bash
python3 sistema_fretes.py
```

## 📁 Arquivos
- `sistema_fretes.py` - Código principal
- `Check_point_1_dados_logistica_RA_final impar.csv` - Dados de entrada
- `README.md` - Documentação do projeto