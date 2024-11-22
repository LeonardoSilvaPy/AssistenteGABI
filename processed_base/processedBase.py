from operator import index

import pandas as pd
import os

from numpy.testing.print_coercion_tables import print_new_cast_table

from preprocessing.preprocessing import preprocessamento


print('Iniciando operação...')

base_census_path = r'C:\Users\Rede14.2\Downloads\telecras_database.csv'
base_census = pd.read_csv(base_census_path, encoding='utf-8')

base_census['Pergunta'] = base_census['Pergunta'].apply(preprocessamento)
base_census['Intenção'] = base_census['Intenção'].apply(preprocessamento)
base_census['Resposta_Pré-definida'] = base_census['Resposta_Pré-definida'].apply(preprocessamento)
base_census['Classificacao'] = base_census['Classificação'].apply(preprocessamento)
base_census['Tokens'] = base_census['Tokens'].apply(preprocessamento)
base_census['Etiqueta'] = base_census['Etiqueta'].apply(preprocessamento)
base_census['Sentimento'] = base_census['Sentimento'].apply(preprocessamento)

directory = 'processed_data'
if not os.path.exists(directory):
    os.makedirs(directory)

processed_data_path = os.path.join(directory, 'base_census_processed.csv')

base_census.to_csv(processed_data_path, index=False, encoding='utf-8')

print(f"Arquivo CSV salvo em: {processed_data_path}")

print(base_census.head())