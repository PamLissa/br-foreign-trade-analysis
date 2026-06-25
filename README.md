# Exportações Brasileiras 2025 - Ciência de Dados

## Perguntas e Hipóteses

### Perguntas

1. Existem padrões sazonais nas exportações brasileiras ao longo dos meses de 2025 em relação ao volume exportado (`net_weight_kg`) e ao valor da exportação (`fob_value_usd`)?

2. É possível classificar a via de transporte principal (`transport_route`) que será utilizada em uma operação de exportação com base nas características físicas da carga (`net_weight_kg`), localização geográfica de origem (`origin_state`) e o valor declarado (`fob_value_usd`)?


### Hipóteses

H1: O volume exportado (`net_weight_kg`) e o valor FOB (`fob_value_usd`) não se distribuem de forma uniforme ao longo do ano, apresentando picos de concentração significativos em meses específicos de 2025 devido à sazonalidade de commodities específicas (`NCM`).

H2: As características físicas da carga (`net_weight_kg`) e a localização geográfica de origem (`origin_state`) são os preditores com maior peso estatístico para classificar a via de transporte (`transport_route`), superando o impacto do valor declarado (`fob_value_usd`).


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
│   └── results/                          # gerado ao executar o notebook
│       └── cleaned_exports_2025.csv
├── milestone-3/
│   ├── notebooks/
│   │   └── export_data_eda.ipynb         # análise exploratória e consultas SQL
│   ├── data/                             # não versionado — ver Download abaixo
│   │   ├── cleaned_exports_2025.csv      # copiar de milestone-2/results/
│   │   └── codigo_vias.csv
│   └── results/                          # gerado ao executar o notebook
│       ├── exports_tidy.parquet
│       └── *.png                         # gráficos das consultas e análises
├── milestone-4/
│   ├── notebooks/
│   │   ├── logreg_rf_modeling.ipynb      # modelagem: Regressão Logística e Random Forest
│   │   └── lightgbm_modeling.ipynb       # modelagem: LightGBM + comparação final dos 3 modelos
│   ├── data/                             # não versionado (obter via milestone-3)
│   │   └── exports_tidy.parquet          # copiar de milestone-3/results/
│   └── results/                          # gerado ao executar os notebooks (gráficos e métricas)
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

**Milestone 3** → `milestone-3/data/`

| Arquivo | Download | Salvar como |
|---|---|---|
| Dataset limpo | copiar `milestone-2/results/cleaned_exports_2025.csv` | `cleaned_exports_2025.csv` |
| Códigos de Vias | https://balanca.economia.gov.br/balanca/bd/tabelas/VIA.csv | `codigo_vias.csv` |

**Milestone 4** → `milestone-4/data/`

O dataset usado na modelagem é o Parquet gerado no milestone-3. Para obtê-lo, execute o milestone-3 e copie o arquivo gerado.

| Arquivo | Origem | Salvar como |
|---|---|---|
| Dataset tidy | executar o milestone-3 e copiar `milestone-3/results/exports_tidy.parquet` | `exports_tidy.parquet` |

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

O dataset limpo será gerado em `milestone-2/results/cleaned_exports_2025.csv`.

### Milestone 3 — Análise exploratória e consultas SQL

```bash
jupyter nbconvert --to notebook --execute --inplace milestone-3/notebooks/export_data_eda.ipynb
```

Os gráficos e o dataset Parquet serão gerados em `milestone-3/results/`.

### Milestone 4: Modelagem com Machine Learning

Requer o dataset tidy em `milestone-4/data/exports_tidy.parquet`. Para obtê-lo, execute o milestone-3 e copie o arquivo gerado:

```bash
cp milestone-3/results/exports_tidy.parquet milestone-4/data/
```

São dois notebooks: a Regressão Logística e o Random Forest em um, e o LightGBM (com a comparação final dos três modelos) no outro. Execute os dois:

```bash
jupyter nbconvert --to notebook --execute --inplace milestone-4/notebooks/logreg_rf_modeling.ipynb
jupyter nbconvert --to notebook --execute --inplace milestone-4/notebooks/lightgbm_modeling.ipynb
```

Os gráficos e métricas serão gerados em `milestone-4/results/`.

## Etapas do Projeto

| Etapa | Descrição | Status |
|---|---|---|
| 1 | Escolha do dataset e definição do problema | Concluída |
| 2 | Integração e limpeza dos dados | Concluída |
| 3 | Análise exploratória e consultas SQL | Concluída |
| 4 | Modelagem com Machine Learning | Concluída |
| 5 | Relatório e comunicação | Em andamento |