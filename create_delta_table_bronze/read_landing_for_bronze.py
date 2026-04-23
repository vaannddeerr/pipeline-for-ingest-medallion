from config_spark.spark_dataset_config import spark_session
from pyspark.dbutils import DBUtils

class CreateTableDelta:
    def __init__(self):
        self.df = None
        self.spark = spark_session

    def read_df(self):
        try:
            dbutils = DBUtils(self.spark)
            path = dbutils.fs.ls("/Volumes/dev/b_bronze/landing/")
            for arquivo in path:
                nome = arquivo.name
                file = nome[:]

                self.df = (self.spark.read
                                    .format('json')
                                    .option('multiline',True)
                                    .load(f'{path}/{file}'))
                
            print(f"Dados carregados. Linhas: {self.df.count()}🔝")    
            return self.df
        
        except:
              print('Falha ao ler o arquivo, arquivo não encontrado')
    
    def write_table(self, tableName:str):
        """Grava o DataFrame atual como uma tabela Delta."""
        if self.df is None:
            raise ValueError("❌Não há dados carregados para gravar! Use ler_tabela primeiro.")
        (self.df.write
                .format('delta')
                .mode('overwrite')
                .option('overwiteSchema', True)
                .saveAsTable(tableName))


