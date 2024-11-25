import spacy
import spacy.training
from spacy.training import Example
import random
import os
import pandas as pd

# Define o caminho onde o modelo treinado será salvo
MODEL_PATH = "../model"

# Caminho absoluto com base na localização do próprio script
BASE_TELECRAS = os.path.join(os.path.dirname(__file__), "../processed_base/processed_data/base_census_processed.csv")
BASE_TELECRAS = os.path.abspath(BASE_TELECRAS)

# Carrega a base de dados e prepara os dados de treinamento
def load_base(path):
    data = pd.read_csv(path)
    data = data[['Pergunta','Intenção']].dropna().drop_duplicates()
    intentions = data['Intenção'].unique()
    training_data = []

# Adiciona cada intenção como rótulo no classificador
    for _, row in data.iterrows():
        categories = {label: (1 if label == row['Intenção'] else 0) for label in intentions}
        training_data.append((row['Pergunta'], {"cats": categories}))

    return training_data, intentions

# Função para treinar o modelo de NLP com os dados carregados
def train(training_data, intentions, output):
    nlp = spacy.blank("pt")

    if "textcat" not in nlp.pipe_names:
        textcat = nlp.add_pipe("textcat", last=True)

    for intention in intentions:
        textcat.add_label(intention)

    nlp.begin_training()

# Treinamento por 250 épocas, com lotes de 34 amostras
    for ep in range(250):
        random.shuffle(training_data)
        losses = {}

 # Divide os dados em lotes (batches) para treinamento
        for batch in spacy.util.minibatch(training_data, size=34):
            exemples = []
            for text, annotations in batch:
                doc = nlp.make_doc(text)
                example = Example.from_dict(doc, annotations)
                exemples.append(example)
            nlp.update(exemples, losses= losses)

        print(f"Epoch {ep} - Losses: {losses}")

 # Salva o modelo treinado no diretório de saída
    if not os.path.exists(output):
        os.makedirs(output)
    nlp.to_disk(output)
    print(f"Modelo salvo em {output}")

# Executa o treinamento se o script for executado diretamente
if __name__ == "__main__":
    training_data, intentions = load_base(BASE_TELECRAS)
    train(training_data, intentions, MODEL_PATH)


