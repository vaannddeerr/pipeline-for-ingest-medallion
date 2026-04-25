from create_delta_table_bronze.read_landing_for_bronze import CreateTableDelta
from dataset_config.spark_dataset import get_path_and_table_name

def pipeline_bronze():
    print('Iniciando a leitura para camada bronze:')
    path,tablename = get_path_and_table_name(env='dev',layer='bronze')
    

    
    res = CreateTableDelta()
    res.df = res.read_df(path)
    print(f'Executa carga para {tablename}')
    res.write_table(tablename)

if __name__=="__main__":
    pipeline_bronze()