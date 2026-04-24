def get_path_and_table_name(env:str, layer:str):
              
        # 1. Lógica Condicional (Ifs) para definir os componentes
        if   env == 'dev':
             env_path = 'dev'
        elif env == 'stg':
             env_path = 'stg'
        elif env == 'prd':
             env_path = 'prd'

        # 2. Definição da pasta e prefixo da camada
        if   layer == 'bronze':
             folder = 'landing'
             prefix = 'b_bronze'
             table_name = 'b_camara_leg'
        elif layer == 'silver':
             folder = 'staging_area'
             prefix = 's_silver'
             table_name = 's_camara_leg'
        elif layer == 'gold':
             folder = 'business'
             prefix = 'g_gold'
             table_name = 'g_camara_leg'

        # 3. Montagem das strings (sem usar o dicionário dentro dos ifs)
        # Exemplo: /volume/dev/b_bronze
        path = f"/Volume/{env_path}/{prefix}/{folder}"


        # Exemplo: dev.b_bronze.b_camara_leg
        tablename = f"{env_path}.{prefix}.{table_name}"

        return path, tablename