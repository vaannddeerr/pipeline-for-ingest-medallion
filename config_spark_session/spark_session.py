from pyspark.sql import SparkSession

def spark_session():
    spark = SparkSession.builder.getOrCreate()
    
    return spark
        
        
        