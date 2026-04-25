from commons.spark_config import spark_session
from pyspark.dbutils import DBUtils


class CreateTableDelta:
    def __init__(self):
        self.df = None
        self.spark = spark_session()
     
        

    def read_df(self, path:str):
        try:
            
            # Lê todos os JSONs da pasta de uma vez
            self.df = self.spark.read.format('json').option('multiline', True).load(path)

            # Criando coluna de registro do arquivo lido
            self.df = self.df.withColumn('filename', self.df['_metadata.file_path'])

            #Verifica se o DataFrame tem linhas
            if self.df.isEmpty():
                raise ValueError("O DataFrame está vazio, nenhum dado foi carregado.")
                
            print(f"Dados carregados. Linhas: {self.df.count()}")
            return self.df
        
        except Exception as e:
            print(f"Erro ao ler os dados: {e}")
            raise e # Isso vai parar o Job no Databricks e mostrar o erro real
    
    def write_table(self, tableName: str):
        try:
            # Garante que tableName é uma string
            
            print(f"Tentando salvar na tabela: {tableName}")
            
            # Usa o formato padrão do Databricks
            self.df.write.format("delta") \
                .mode("overwrite") \
                .saveAsTable(tableName)
                
            print("Sucesso ao gravar!")
        except Exception as e:
            print(f"Erro ao gravar na tabela: {e}")
            raise e


