from consuming_api_data.capture_data import CaptureApiData


def executa_pipeline(path):
    file_path = f'dadosabertos_{path}.json'
    path = f'/Volumes/dev/b_bronze/landing/{file_path}'
    print('🔛Iniciando processamento.🔛')
    print('================================')
    menager = CaptureApiData(url='https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome')


    resultado = menager.capture_api()
    print(f'📖Resultado da solicitação:')

    menager.save_out(path, resultado)
    print(f'✔️Arquivo salvo com sucesso')

if __name__=="__main__":
    executa_pipeline()   
