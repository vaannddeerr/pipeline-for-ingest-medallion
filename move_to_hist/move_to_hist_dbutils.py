from pyspark.dbutils import DBUtils
from commons.spark_config import spark_session
from dataset_config.spark_dataset import get_path_and_table_name



def move_to_hist():
    spark = spark_session()
    dbutils = DBUtils(spark)
    
    path, _ = get_path_and_table_name(env='dev', layer='bronze')
    origem = f'{path}/'
    destino = f'{path}/move_to_hist/'
    
    # Cria a pasta de destino se ela ainda não existir
    dbutils.fs.mkdirs(destino)
    
    # Lista todos os conteúdos da pasta de origem
    arquivos = dbutils.fs.ls(origem)
    
    for arquivo in arquivos:
        # 1. Verifica se o nome NÃO é 'move_to_hist/' para evitar mover a pasta de destino pra dentro dela mesma
        # 2. Verifica se o nome NÃO é um diretório de metadados do Spark (como _delta_log ou _temporary)
        if arquivo.name != "move_to_hist/" and not arquivo.name.startswith("_"):
            if arquivo.name in arquivo.name.endswith(".json"):
                dbutils.fs.mv(arquivo.path, destino + arquivo.name)
                print(f"Arquivo {arquivo.name} movido com sucesso.")