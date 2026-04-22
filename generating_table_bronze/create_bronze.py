from pyspark.sql import functions as F



def create_table_bronze(menager):
    df = (
            menager.spark
                    .read
                    .format('json')
                    .load(menager.path)
          
         )

    return df.show()
