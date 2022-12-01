import numpy as np
import pandas as pd


class censoService():
    def __init__(self) -> None:
        pass

    def union_df():
        df_censo_estado = pd.read_csv('search_source\censo_estado.csv')
        df_rouanet = pd.read_csv('search_source/rouanet.csv')

        print('df_censo_estado --->')
        print(df_censo_estado)

        print('df_rouanet --->')
        print(df_rouanet)

        df_censo_estado['estado_ibge'] = df_censo_estado['codigo']

        df = pd.merge(df_censo_estado, df_rouanet, how='inner', on='estado_ibge')
        
        df = dict_uf(df)
        

        print(df)
        print(df.dtypes)


def dict_uf(df):
    
    dict_states = {'Acre': 'AC',
    'Alagoas' : 'AL',
    'Amapá' : 'AP',
    'Amazonas' : 'AM',
    'Bahia' : 'BA',
    'Ceará' : 'CE',
    'Distrito Federal' : 'DF',
    'Espírito Santo' : 'ES',
    'Goiás' : 'GO',
    'Maranhão' : 'MA',
    'Mato Grosso' : 'MT',
    'Mato Grosso do Sul' : 'MS',
    'Minas Gerais' : 'MG',
    'Pará' : 'PA',
    'Paraíba' : 'PB',
    'Paraná' : 'PR',
    'Pernambuco' : 'PE',
    'Piauí' : 'PI',
    'Rio de Janeiro' : 'RJ',
    'Rio Grande do Norte' : 'RN',
    'Rio Grande do Sul' : 'RS',
    'Rondônia' : 'RO',
    'Roraima' : 'RR',
    'Santa Catarina' : 'SC',
    'São Paulo' : 'SP',
    'Sergipe' : 'SE',
    'Tocantins' : 'TO'
    }


    for states in df['estado']:
        df = df.replace(states, dict_states[states])
    
    return df

