# Exportações Brasileiras 2025 — Ciência de Dados

**Alunas:** Pamella Lissa Sato Tamura (2254107) e Raquel de Oliveira (2399113)

## Estrutura

```
br-foreign-trade-analysis/
├── milestone-1/
│   ├── data/                             # não versionado — ver Download abaixo
│   └── export_data_overview.py           # análise exploratória inicial (CLI)
├── milestone-2/
│   ├── notebooks/
│   │   └── export_data_wrangling.ipynb   # limpeza e integração dos dados
│   ├── data/                             # não versionado — ver Download abaixo
│   │   ├── exportacao_2025.csv
│   │   ├── codigo_ncm.csv
│   │   └── codigo_pais.csv
├── .gitignore
├── requirements.txt
└── README.md
```

## Download dos Dados

Os arquivos de dados não são versionados. Baixe e salve conforme indicado:

**Milestone 1** → `milestone-1/data/`

| Arquivo | Download | Salvar como |
|---|---|---|
| Exportações 2025 | https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_2025.csv | `exportacao_2025.csv` |

**Milestone 2** → `milestone-2/data/`

| Arquivo | Download | Salvar como |
|---|---|---|
| Exportações 2025 | https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_2025.csv | `exportacao_2025.csv` |
| Códigos NCM | https://balanca.economia.gov.br/balanca/bd/tabelas/NCM.csv | `codigo_ncm.csv` |
| Códigos de Países | https://balanca.economia.gov.br/balanca/bd/tabelas/PAIS.csv | `codigo_pais.csv` |

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

### Milestone 2 — Limpeza e integração

```bash
jupyter nbconvert --to notebook --execute --inplace milestone-2/notebooks/export_data_wrangling.ipynb
```

## Etapas do Projeto

| Etapa | Descrição | Status |
|---|---|---|
| 1 | Escolha do dataset e definição do problema | Concluída |
| 2 | Integração e limpeza dos dados | Em Andamento |
| 3 | Análise exploratória e consultas SQL | — |
| 4 | Modelagem com Machine Learning | — |
| 5 | Relatório e comunicação | — |