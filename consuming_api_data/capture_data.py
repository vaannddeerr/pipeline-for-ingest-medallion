
import requests
import json
from datetime import datetime, timedelta

class CaptureApiData:
    def __init__(self, url:str):
        self.url = url
        self.response = None
        self.error = None
        self.path = None

    def capture_api(self):
        try:
            res = requests.get(self.url, timeout=30)
            res.raise_for_status()
            self.response = res.json()
            self.error = 'Nenhum'
            return self.response
        
        except Exception as e:
            self.erro = str(e)
            self.response = None
            return None
            print(f"Erro na comunicação com a API: {self.error}")

    def save_out(self, path:str, response:str):

        archive = datetime.now() + timedelta(hours=-3)
        archive = str(archive)
        archive = archive[0:19]

        path = f'{archive}'

        if response:
            with open(path,'w', encoding='utf-8') as outputResponse:
                json.dump(response, outputResponse, indent=4, ensure_ascii=False)

            print(f"Local onde o arquivo foi salvo: '{path}'✍️")
        else:
            print(f"Não foi possível salvar. Erro: {self.error}")

    



        