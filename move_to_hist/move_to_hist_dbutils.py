from pyspark.dbutils import DBUtils
from commons.spark_config import spark_session
from dataset_config.spark_dataset import get_path_and_table_name


def move_to_hist():
    spark = spark_session()
    dbutils = DBUtils(spark)

    path,_ = get_path_and_table_name(env='dev',layer='bronze')
    print(path)
    destino = '/Volumes/dev/b_bronze/move_to_hist/'
    print(destino)
    dbutils.fs.mkdirs(destino)
    return dbutils.fs.mv(origem, destino,recurse=True)

move_to_hist()