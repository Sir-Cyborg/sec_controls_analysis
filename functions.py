from rake_nltk import Rake
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

def crea_pool_keywords(descrizioni, top_n=20, lingua='italian'):
    """
    Estrae un pool di parole singole rilevanti da una stringa contenente descrizioni.
    
    :param descrizioni: stringa unica con tutte le descrizioni
    :param top_n: numero massimo di keyword da restituire
    :param lingua: lingua per le stopwords (default: 'italian')
    :return: dizionario con parole chiave (singole)
    """
    rake = Rake()
    keyword_counter = Counter()
    
    # Applica RAKE normalmente
    rake.extract_keywords_from_text(descrizioni)
    keywords = rake.get_ranked_phrases()  # Frasi candidate

    # Prepara stopwords e punteggiatura
    stop_words = set(stopwords.words(lingua))
    punctuation = set(string.punctuation)

    # Tokenizza le frasi e filtra parole
    for frase in keywords:
        parole = word_tokenize(frase.lower())
        parole_filtrate = [
            p for p in parole 
            if p not in stop_words and p not in punctuation and len(p) > 2
        ]
        keyword_counter.update(parole_filtrate)

    # Seleziona le top-N parole
    pool = [kw for kw, _ in keyword_counter.most_common(top_n)]

    result = {"pool_keywords": pool}
    return result

import nltk
nltk.download('punkt')
nltk.download('stopwords')
