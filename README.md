# Exportações Brasileiras 2025 — Ciência de Dados

**Alunas:** Pamella Lissa Sato Tamura (2254107) e Raquel de Oliveira (2399113)

## Estrutura

```
br-foreign-trade-analysis/
├── milestone-1/
│   ├── data/                             # não versionado — ver Download abaixo
│   └── export_data_overview.py           # análise exploratória inicial (CLI)
├── .gitignore
├── requirements.txt
└── README.md
```

## Download dos Dados

Os arquivos de dados não são versionados. Baixe-os e salve em `milestone-1/data/` com os nomes indicados:

| Arquivo | Download | Salvar como |
|---|---|---|
| Exportações 2025 | https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_2025.csv | `exportacao_2025.csv` |

## Como executar

### Dependências

```bash
pip install -r requirements.txt
```

### Milestone 1 — Análise exploratória inicial

Script CLI que imprime um overview completo de qualquer CSV: shape, tipos, missing values, estatísticas numéricas, cardinalidade e checklist de requisitos mínimos do projeto.

```bash
python milestone-1/export_data_overview.py milestone-1/data/exportacao_2025.csv
```

## Etapas do Projeto

| Etapa | Descrição | Status |
|---|---|---|
| 1 | Escolha do dataset e definição do problema | Concluída |
| 2 | Integração e limpeza dos dados | Concluída |
| 3 | Análise exploratória e consultas SQL | — |
| 4 | Modelagem com Machine Learning | — |
| 5 | Relatório e comunicação | — |