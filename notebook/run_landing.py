from consuming_api_data.capture_data import CaptureApiData
from dataset_config.spark_dataset import get_path_and_table_name



def executa_pipeline():
    
    print('🔛Iniciando processamento.🔛')
    print('================================')
    menager = CaptureApiData(url='https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome')
    
    resultado = menager.capture_api()
    print(f'📖Resultado da solicitação:')

    menager.path = get_path_and_table_name(env='dev',layer='bronze')

    menager.save_out(menager.path, resultado)
    print(f'✔️Arquivo salvo com sucesso')


    
    



if __name__=="__main__":
    executa_pipeline()   
