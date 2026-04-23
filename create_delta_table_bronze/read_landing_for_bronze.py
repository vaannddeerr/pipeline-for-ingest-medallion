from config_spark.spark_dataset_config import spark_session

class CreateTableDelta:
    def __init__(self):
        self.df = None
        self.spark = spark_session

    def read_df(self):
        try:
            path = dbutils.fs.ls("/Volumes/dev/b_bronze/landing/")
            for arquivo in path:
                tam = arquivo.size
                nome = arquivo.name
                file = nome[:]

                self.df = (self.spark.read
                                    .format('json')
                                    .option('multiline',True)
                                    .load(file))
        except:
              print('Falha ao ler o arquivo, arquivo não encontrado')
    
    def write_table(self):
        (self.df.write
                .format('delta')
                .mode('overwrite')
                .option('overwiteSchema', True)
                .saveAsTable('b_bronze.tb_dadosabertos'))


