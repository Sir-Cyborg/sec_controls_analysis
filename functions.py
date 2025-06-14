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
    stop_words = set(stopwords.words(lingua))
    punctuation = set(string.punctuation)

    # Step 1: Tokenizza e filtra parole rilevanti
    parole = word_tokenize(descrizioni.lower())
    parole_filtrate = [
        p for p in parole 
        if p not in stop_words and p not in punctuation and len(p) > 2
    ]

    # Ricostruisci una stringa pulita
    testo_pulito = " ".join(parole_filtrate)

    # Step 2: Applica RAKE sulla stringa pulita
    rake = Rake()
    keyword_counter = Counter()

    rake.extract_keywords_from_text(testo_pulito)
    keywords = rake.get_ranked_phrases()

    # Tokenizza ancora per ottenere solo parole singole da frasi di RAKE
    for frase in keywords:
        parole = word_tokenize(frase)
        keyword_counter.update(parole)

    # Seleziona le top-N parole
    pool = [kw for kw, _ in keyword_counter.most_common(top_n)]

    result = {"pool_keywords": pool}
    return result

""""
import nltk
nltk.download('punkt')
nltk.download('stopwords')
"""