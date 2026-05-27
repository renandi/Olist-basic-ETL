import csv, math, re, datetime

# Leitor de csv
def read_csv(filename: str):
    """Carrega um arquivo csv em uma lista.
    
    Args:
        filename : Caminho do arquivo.
        
    Returns:
        mylist : Lista de dicionários, onde cada elemento da lista \
            representa uma linha do dataset.
    """
    with open(filename, 'r') as file:
        mylist = []
        reader = csv.DictReader(file)
        mylist = list(reader)
        return mylist


# Preencher categorias faltantes
def fill_missing_category_name(product_list : list) -> int :
    """Encontra produtos com categoria faltante e substitui por \"sem categoria\".
    
    Args:
        product_list: Lista de produtos, onde cada item da lista é um dicionário.
        
    Returns:
        missing_count: Número de produtos alterados.
    """
    
    missing_count = 0
    
    for product in product_list:
        if (product["product_category_name"] == "" or product["product_category_name"] == None):
            product["product_category_name"] = "sem categoria"
            missing_count = missing_count + 1
    
    print (f"Produtos com categorias faltantes alterados: {missing_count}")
    
    return missing_count


# Verificar produtos com dimensoes fisicas faltantes
def check_missing_product_dimensions(product_list : list, dimensions_columns : list):
    """Verificar quantos produtos tem dimensões físicas faltantes.
    
    Args: 
        product_list: Lista de produtos.
        dimension_columns: Lista de nomes das colunas de dimensões.
    """
    
    missing_dimensions_count_dict = {dim : 0  for dim in dimensions_columns}

    missing_indices = []

    for i, product in enumerate(product_list):
        for dimension in dimensions_columns:
            
            if len(product[dimension]) == 0:                
                missing_dimensions_count_dict[dimension] = missing_dimensions_count_dict[dimension] + 1
                missing_indices.append({i: dimension})
    
    missing_count = sum (missing_dimensions_count_dict.values())

    if (missing_count > 0):
        print (f"\nProdutos com dimensões faltantes encontrados: \n{missing_dimensions_count_dict}")
    else:
        print("Nenhum produto com dimensão faltante encontrado.")


#  
def handle_missing_product_dimensions(products : list, dimensions_columns : list) -> int:
    """Remove produtos com valores faltantes nas colunas especificadas.
    
    Args: 
        product_list: Lista de produtos.
        dimension_columns: Lista de nomes das colunas de dimensões.
    """
    
    missing_dimensions_count_dict = {dim : 0  for dim in dimensions_columns}
    
    missing_indices = []
    
    for i, product in enumerate(products):
        for dimension in dimensions_columns:
            
            if len(product[dimension]) == 0:
            
                missing_dimensions_count_dict[dimension] = missing_dimensions_count_dict[dimension] + 1
                
                missing_indices.append({i: dimension})
                
                # Remover
                products.pop(i)
                break
    
    missing_dimensions_count = sum (missing_dimensions_count_dict.values())

    if (missing_dimensions_count > 0):
        print (f"Produtos com dimensões faltantes removidos: {missing_dimensions_count}")
    else:
        print("Nenhum produto com dimensão faltante encontrado.")
        
    return missing_dimensions_count


def category_patternization(products : list):
    """Ajusta coluna de categorias para letras minusculas e sem caracteres especiais.
    
    Args:
        products: Lista de produtos.
    """
    for p in products:
        p["product_category_name"] = p["product_category_name"].lower()
        p["product_category_name"] = re.sub(r'[^a-zA-Z0-9\s]', '',p["product_category_name"])


def clean_text_columns(target_list : list, text_columns_list : list):
    """Limpar espaços nas extremidades das strings das colunas passadas. 
    
    Args:
        target_list: A lista de dicionários contendo os dados.
        text_columns_list: Lista contendo os nomes das colunas a serem processadas.
    """
    for p in target_list:        
        for col in text_columns_list:
            p[col] = p[col].strip()


def convert_numeric_columns(target_list : list, numeric_columns_list : list):
    """Converte as colunas de string da lista de dados especificadas na lista numérica para float.
    
    Args:
        target_list: A lista de dicionários contendo os dados.
        numeric_columns_list: Lista contendo os nomes das colunas a serem convertidas para float.
    """
    for p in target_list:
        for col in numeric_columns_list:
            if p[col] is None or p[col] == '':
                p[col] = 0.0
            else:
                p[col] = float(p[col])


def convert_date_to_br_fmt(target_list : list, columns : list):
    """Converte as colunas de string da lista de dados especificadas \
        para formato de data simplificado brasileiro.
    
    Args:
        target_list: A lista de dicionários contendo os dados.
        columns: Lista contendo os nomes das colunas a serem convertidas.
    """
    for o in target_list:
        for col in columns:
            if o[col] is None or o[col] == '':
                continue
            else:
                dt = datetime.datetime.strptime(o[col], '%Y-%m-%d %H:%M:%S')
                o[col] = f'{dt.day}/{dt.month}/{dt.year}'