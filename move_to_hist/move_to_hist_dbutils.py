from pyspark.dbutils import DBUtils
from commons.spark_config import spark_session

def move_to_hist(menager):
    spark = spark_session()
    dbutils = DBUtils(spark)
    path = path[:-26]
    menager.path = path +'*'
    return dbutils.fs.mv(f'{menager.path}','/Volumes/move_to_hist/',recurse=True)

move_to_hist(menager.path)