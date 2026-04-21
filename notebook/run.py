from consuming_api_data.capture_data import CaptureApiData


def executa_pipeline():
    
    print('🔛Iniciando processamento.🔛')
    print('================================')
    menager = CaptureApiData(url='https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome')
    
    file_path = 'dadosabertos_'+ menager.path +'.json'
    menager.path = f'/Volumes/dev/b_bronze/landing/{file_path}'
    
    

    resultado = menager.capture_api()
    print(f'📖Resultado da solicitação:')

    menager.save_out(menager.path, resultado)
    print(f'✔️Arquivo salvo com sucesso')

if __name__=="__main__":
    executa_pipeline()   
