from create_delta_table_bronze.read_landing_for_bronze import CreateTableDelta

def pipeline_bronze():
    print('Iniciando a leitura para gravação da tabela bronze:')

    catalog = 'dev'
    print(f'Catalog(UC): {catalog}')

    schema = 'b_bronze'
    print(f'Database: {schema}')

    table = 'tb_camara_leg'
    print(f'Delta Table: {table}')

    tablename = f'{catalog}.{schema}.{table}'
    print(f'Table Name: {tablename}')

    print('')
    res = CreateTableDelta()
    res.df = res.read_df()
    res.write_table(tablename)

if __name__=="__main__":
    pipeline_bronze()