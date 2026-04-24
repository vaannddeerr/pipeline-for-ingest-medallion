from pyspark.dbutils import DBUtils
from commons.spark_config import spark_session

def move_to_hist(menager):
    spark = spark_session()
    dbutils = DBUtils(spark)

    return dbutils.fs.mv(f'{menager.path}','/Volumes/move_to_hist/')

move_to_hist(menager.path)