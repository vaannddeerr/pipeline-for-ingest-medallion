from pyspark.dbutils import DBUtils
from commons.spark_config import spark_session
from dataset_config.spark_dataset import get_path_and_table_name
import os

# Exemplo: o path vem dinamicamente da sua função
# Ex: '/Volumes/dev/b_bronze/landing/dadosabertos.json'
path,_ = get_path_and_table_name(env='dev', layer='bronze') 

# 1. Obtenha o diretório onde o arquivo está (o 'landing')
dir_atual = os.path.dirname(path) 

# 2. Obtenha o diretório pai (o 'b_bronze')
# Isso garante que você está dentro do volume correto, não importa o nome do volume
base_volume = os.path.dirname(dir_atual)

# 3. Construa o destino dinamicamente
# Isso mantém a estrutura: /Volumes/dev/b_bronze/move_to_hist/
destino = os.path.join(base_volume, 'move_to_hist/')

# Agora seu código é 100% dinâmico e respeita a estrutura do Databricks!
spark = spark_session()
dbutils = DBUtils(spark)
dbutils.fs.mkdirs(destino)
dbutils.fs.mv(path + '*', destino, recurse=True)


# def move_to_hist():
#     spark = spark_session()
#     dbutils = DBUtils(spark)

#     path,_ = get_path_and_table_name(env='dev',layer='bronze')
#     path_destino = path[:-43]
#     path = path[:-26]
#     origem = path +'*'
#     destino = path_destino +'move_to_hist/'
#     dbutils.fs.mkdirs(destino)
#     return dbutils.fs.mv(origem, destino,recurse=True)

# move_to_hist()