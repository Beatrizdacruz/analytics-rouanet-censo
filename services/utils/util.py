class Util():
    def __init__(self, df) -> None:
        self.df = df

    def drop_values(df):

        df = df[~df.valor_em_reais.eq(0)]
        df = df[~df.quantidade.eq(0)]

        return df

    def surrogate(df):
        df['sk_order'] = df.index + 1

        return df

    def drop_duplicates_report(df):
        df = df.drop_duplicates()

        return df

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

