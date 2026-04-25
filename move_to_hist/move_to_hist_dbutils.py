from pyspark.dbutils import DBUtils
from commons.spark_config import spark_session
from dataset_config.spark_dataset import get_path_and_table_name


def move_to_hist():
    spark = spark_session()
    dbutils = DBUtils(spark)

    path,_ = get_path_and_table_name(env='dev',layer='bronze')
    path_detino = path[:-43]
    path = path[:-26]
    origem = path +'*'
    destino = path_detino +'move_to_hist/'
    dbutils.fs.mkdirs(destino)
    return dbutils.fs.mv(origem, destino,recurse=True)

move_to_hist()