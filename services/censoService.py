import numpy as np
import pandas as pd
from services.utils.util import Util


class censoService():
    def __init__(self, df) -> None:
        self.df = df

    def union_df():
        try:
            df_censo_estado = pd.read_csv('search_source\censo_estado.csv')
            df_rouanet = pd.read_csv('search_source/rouanet.csv')

            print('df_censo_estado --->')
            print(df_censo_estado)

            print('df_rouanet --->')
            print(df_rouanet)

            df_censo_estado['estado_ibge'] = df_censo_estado['codigo']

            df = pd.merge(df_censo_estado, df_rouanet, how='inner', on='estado_ibge')
            
            df = Util.surrogate(df)

            df = Util.drop_values(df)

            df = Util.dict_uf(df)
            
            df.to_csv('relatorio_censo_rouanet.csv', index=False)
            

            print(df)
            print(df.dtypes)

            return df
        except Exception as e:
            return e
            

