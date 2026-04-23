import os
from pyspark.dbutils import DBUtils
from commons.spark_config import spark_session

spark = spark_session()
dbutils = DBUtils(spark)

# CRIAÇÃO DO WIDGET
# Isso força a criação de um menu dropdown no Databricks com os ambientes válidos.
try:
    dbutils.widgets.dropdown("env", "dev", ["dev", "homolog", "prod"])
    CURRENT_ENV = dbutils.widgets.get("env")
except:
    # Se rodar localmente no VS Code (sem dbutils), cai aqui e assume 'dev'
    CURRENT_ENV = 'dev'
    
# Define o ambiente (busca no sistema, padrão é 'dev')
# Para mudar em produção, basta definir a variável de ambiente ENV=prod
CURRENT_ENV = os.getenv('ENV', 'dev')

# Configurações por ambiente (Base de dados / Catálogos)
# Se você tiver regras diferentes para cada um, adicione aqui
CONFIG_BY_ENV = {
    'dev': {'catalog': 'dev', 'schema_prefix': 'b_'},
    'stg': {'catalog': 'stg', 'schema_prefix': 'h_'},
    'prd': {'catalog': 'prd', 'schema_prefix': 'p_'}
}

# Validação simples
env_cfg = CONFIG_BY_ENV.get(CURRENT_ENV, CONFIG_BY_ENV['dev'])

# Estrutura centralizada dos datasets
DATA_PIPELINE_CONFIG = {
    "bronze": {
        "catalog": env_cfg['catalog'],
        "schema": f"{env_cfg['schema_prefix']}bronze",
        "table": "tb_camara_leg"
    },
    "silver": {
        "catalog": env_cfg['catalog'],
        "schema": f"{env_cfg['schema_prefix']}silver",
        "table": "tb_camara_leg"
    },
    "gold": {
        "catalog": env_cfg['catalog'],
        "schema": f"{env_cfg['schema_prefix']}gold",
        "table": "tb_camara_leg"
    }
}

# Montagem da string
def get_table_name(layer):
    if layer not in DATA_PIPELINE_CONFIG:
        raise ValueError(f"Camada '{layer}' não encontrada na configuração!")
    
    c = DATA_PIPELINE_CONFIG[layer]
    return f"{c['catalog']}.{c['schema']}.{c['table']}"