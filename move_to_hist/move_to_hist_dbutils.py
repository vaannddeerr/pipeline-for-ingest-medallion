from pyspark.dbutils import DBUtils
from commons.spark_config import spark_session
from dataset_config.spark_dataset import get_path_and_table_name



def move_to_hist():
    spark = spark_session()
    dbutils = DBUtils(spark)
    
    path, _ = get_path_and_table_name(env='dev', layer='bronze')
    origem = f'{path}/'
    destino = f'{path}/move_to_hist/'
    
    print(f"DEBUG - Origem: {origem}")
    print(f"DEBUG - Destino: {destino}")
    
    arquivos = dbutils.fs.ls(origem)
    
    for arquivo in arquivos:
        print(f"DEBUG - Analisando: {arquivo.name}")
        
        # Filtros de segurança
        if (arquivo.name != "move_to_hist/" and 
            not arquivo.name.startswith("_") and 
            arquivo.name.endswith(".json")):
            
            caminho_final = destino + arquivo.name
            print(f"DEBUG - Movendo de {arquivo.path} para {caminho_final}")
            
            dbutils.fs.mv(arquivo.path, caminho_final)
        else:
            print(f"DEBUG - Ignorado: {arquivo.name}")

move_to_hist()