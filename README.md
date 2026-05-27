# Olist Dataset ETL 

## Machine Learning e Visão Computacional - Mini Projeto

Limpeza e tratamento de dados dos arquivos do dataset da Olist `olist_products_dataset` e `olist_orders_dataset` utilizando apenas bibliotecas nativas do Python como `csv`, `re` e `datetime`.

---

## Descrição do Projeto

A **Olist** opera como uma plataforma de e-commerce que integra lojistas a grandes marketplaces. Com um volume massivo de transações diárias, os dados brutos frequentemente apresentam inconsistências, registros duplicados, valores nulos e formatações de data ou texto fora do padrão. 

O objetivo deste script é automatizar o processo de **ETL (Extract, Transform, Load)**, aplicando regras de negócio para limpar e padronizar os dados de produtos e pedidos. Ao final da execução, o notebook gera um conjunto de dados tratado e mostra um resumo das principais mudanças.

---

## Guia de Execução

Siga os passos abaixo para rodar o projeto de limpeza de dados em sua máquina local. Como o projeto utiliza exclusivamente a biblioteca padrão do Python, **não é necessário instalar dependências externas**.

### 1. Pré-requisitos
* Ter o **Python 3.x** instalado no seu sistema.
* Ter o Jupyter Notebook instalado (ou usar o VS Code / Google Colab para abrir o arquivo `.ipynb`).

### 2. Organização dos Arquivos
Certifique-se de que a estrutura do seu projeto está organizada da seguinte forma antes de começar:
```text
📂 main-repo
 ├──📂 data
 │   ├── olist_products_dataset.csv
 ├───└── olist_orders_dataset.csv
 ├── main.ipynb
 └── funcs.py
```

## Reflexão Teórica: Por que limpar os dados importa para a IA?

Em projetos de Machine Learning, existe uma regra de ouro que resume a importância crítica da etapa de engenharia e limpeza de dados: se alimentarmos o modelo com dados ruins, ele resultará em resultados ruins (Garbage In, Garbage Out). Uma lógica de programação robusta aplicada ao tratamento inicial do dataset impede que inconsistências e "ruídos" sejam interpretados pelo modelo como padrões reais. Se treinarmos um algoritmo com dados redundantes, mal tratados ou correlações espúrias geradas por falhas de preenchimento, o modelo sofrerá de Overfitting, decorando as imperfeições da base de treino e perdendo totalmente a capacidade de generalizar para novos dados do mundo real.

Além disso, a limpeza criteriosa é a principal linha de defesa contra o Viés (bias) em Inteligência Artificial. Valores nulos mal interpretados ou a presença desproporcional de categorias mal formatadas podem induzir o modelo a tomar decisões sistematicamente errôneas ou preconceituosas contra determinados grupos. Garantir o tratamento correto de strings, a padronização de datas com datetime e a filtragem de anomalias via expressões regulares (re) assegura que o futuro modelo de aprendizado de máquina aprenda com uma base estatisticamente íntegra, resultando em previsões mais justas, precisas e confiáveis.
