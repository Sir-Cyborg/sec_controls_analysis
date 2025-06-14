from tabulate import tabulate
from rake_nltk import Rake
import nltk
from collections import Counter

# Stampa in formato tabellare
def stampa(data):
    print(tabulate(data, headers='keys', tablefmt='fancy_grid', showindex=True))



def crea_pool_keywords(descrizioni, top_n=20):
    """
    Estrae un pool di keyword da un insieme di descrizioni.
    
    :param descrizioni: unica stringa che contiene descrizioni dei controlli
    :param top_n: numero massimo di keyword da restituire
    :return: dizionario con keyword e (opzionale) sentiment medio
    """
    rake = Rake()
    keyword_counter = Counter()


    rake.extract_keywords_from_text(descrizioni)
    keywords = rake.get_ranked_phrases()
    keyword_counter.update(keywords)


    # Seleziona le top N keyword più frequenti
    pool = [kw for kw, _ in keyword_counter.most_common(top_n)]

    result = {"pool_keywords": pool}
    return result

#import nltk
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('punkt_tab')