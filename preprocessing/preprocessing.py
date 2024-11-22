import spacy
import string

from spacy.lang.pt.stop_words import STOP_WORDS

stop_words = STOP_WORDS

pontuacoes = string.punctuation
pln = spacy.load('pt_core_news_sm')

def preprocessamento(texto):
  texto = texto.lower()
  documento = pln(texto)

  lista = []
  for token in documento:
    lista.append(token.lemma_)

  lista = [palavra for palavra in lista if palavra not in stop_words
           and palavra not in pontuacoes]
  lista = ' '.join([str(elemento) for elemento in lista if not elemento.isdigit()])

  returnlista