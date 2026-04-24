from pyspark.dbutils import DBUtils
from commons.spark_config import spark_session
from dataset_config.spark_dataset import get_path_and_table_name


def move_to_hist():
    spark = spark_session()
    dbutils = DBUtils(spark)
    
    path,_ = get_path_and_table_name(env='dev',layer='bronze')
    path = path[:-26]
    path = path +'*'
    return dbutils.fs.mv(f'{path}','/Volumes/move_to_hist/',recurse=True)

move_to_hist()