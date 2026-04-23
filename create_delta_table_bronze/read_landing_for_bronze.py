from config_spark.spark_dataset_config import spark_session
from pyspark.dbutils import DBUtils
from pyspark.sql.functions import input_file_name

class CreateTableDelta:
    def __init__(self):
        self.df = None
        self.spark = spark_session()
        

    def read_df(self):
        try:
            path = "/Volumes/dev/b_bronze/landing/"
            # Lê todos os JSONs da pasta de uma vez
            self.df = self.spark.read.format('json').option('multiline', True).load(path)

            # Criando coluna de registro do arquivo lido
            self.df = self.df.withColumn('filename', input_file_name())

            #Verifica se o DataFrame tem linhas
            if self.df.isEmpty():
                raise ValueError("O DataFrame está vazio, nenhum dado foi carregado.")
                
            print(f"Dados carregados. Linhas: {self.df.count()}")
            return self.df
        
        except Exception as e:
            print(f"Erro ao ler os dados: {e}")
            raise e # Isso vai parar o Job no Databricks e mostrar o erro real
    
    def write_table(self, tableName:str):
        """Grava o DataFrame atual como uma tabela Delta."""
        if self.df is None:
            raise ValueError("❌Não há dados carregados para gravar! Use ler_tabela primeiro.")
        (self.df.write
                .format('delta')
                .mode('overwrite')
                .option('overwiteSchema', True)
                .saveAsTable(tableName))


