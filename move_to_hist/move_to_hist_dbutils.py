from pyspark.dbutils import DBUtils
from commons.spark_config import spark_session
from dataset_config.spark_dataset import get_path_and_table_name


def move_to_hist():
    spark = spark_session()
    dbutils = DBUtils(spark)

    path,_ = get_path_and_table_name(env='dev',layer='bronze')

    origem = f'{path}/'
    print(f'Caminho origem: {origem}/')

    destino = f'{path}/move_to_hist/'
    print(f'Caminho destino: {destino}/')

    dbutils.fs.mkdirs(destino)
    return dbutils.fs.mv(origem, destino,recurse=True)

move_to_hist()