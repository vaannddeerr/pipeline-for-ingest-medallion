from pyspark.dbutils import DBUtils
from commons.spark_config import spark_session
from dataset_config.spark_dataset import get_path_and_table_name
import os

# Exemplo de path: '/Volumes/dev/b_bronze/landing/dadosabertos.json'
path,_ = get_path_and_table_name(env='dev', layer='bronze')

# 1. Obtém a pasta pai: '/Volumes/dev/b_bronze/landing'
dir_atual = os.path.dirname(path)

# 2. Obtém a base do volume: '/Volumes/dev/b_bronze'
# Isso garante que estamos dentro do schema 'b_bronze'
base_volume = os.path.dirname(dir_atual)

# 3. Define o destino explicitamente dentro do volume b_bronze
# Isso resulta em: '/Volumes/dev/b_bronze/move_to_hist/'
destino = os.path.join(base_volume, 'move_to_hist')

# 4. CRÍTICO: Certifique-se de que o caminho termine com '/' para o dbutils
destino_path = destino + '/'

# 5. Executa
spark = spark_session()
dbutils = DBUtils(spark)
dbutils.fs.mkdirs(destino_path)
dbutils.fs.mv(path + '*', destino_path, recurse=True)

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