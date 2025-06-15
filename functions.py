from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import numpy as np
import string
from tabulate import tabulate

def estrai_keywords_bert(text, top_n=10, lingua='italian'):
    # Carica modello BERT pre-addestrato per embedding frasi/parole
    model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

    # Prepara stopwords e punteggiatura
    stop_words = set(stopwords.words(lingua))
    punctuation = set(string.punctuation)

    # Tokenizza e filtra parole
    parole = word_tokenize(text.lower())
    parole_filtrate = [p for p in parole if p not in stop_words and p not in punctuation and len(p) > 2]

    # Embedding del testo intero
    embedding_testo = model.encode([text])[0]

    # Embedding di ogni parola singola
    embedding_parole = model.encode(parole_filtrate)

    # Calcola similarità coseno tra ogni parola e il testo
    sim = cosine_similarity([embedding_testo], embedding_parole)[0]

    # Seleziona top N parole più simili
    top_indices = np.argsort(sim)[-top_n:][::-1]
    keywords = [parole_filtrate[i] for i in top_indices]

    return keywords

"""""
# Esempio d’uso
testo = "Verifica la presenza di malware, autenticazione a due fattori e protezione delle password."
print(estrai_keywords_bert(testo, top_n=5))
"""

# Stampa in formato tabellare
def stampa(data):
    print(tabulate(data, headers='keys', tablefmt='fancy_grid', showindex=True))